from asm.Label import Label
from type.Type import Type
from type.TypeTable import TypeTable
from abst.ASTVisitor import ASTVisitor
import abst
import ir
import entity
import exception
import utils

class IRGenerator(ASTVisitor):
    def __init__(self,tt,eh):
        self.ttable = tt
        self.eh = eh

        self.stmts = []
        self.scope_stack = []
        self.break_stack = []
        self.continue_stack = []
        self.jump_map = dict()

        self.expr_nest_level = 0
    
    def type_table(self):
        return self.ttable
    def error_handler(self):
        return self.eh
    

    def generate(self,ast):
        for var in ast.defined_variables():
            if var.has_initializer():
                var.set_IR(self.transform_expr(var.initializer()))
        for f in ast.defined_functions():
            f.set_IR(self.compile_function_body(f))
        if self.eh.error_occured():
            raise SemanticException("IR generation failed.")
        return ast.ir()
    

    def compile_function_body(self,f):
        self.stmts = []
        self.scope_stack = []
        self.break_stack = []
        self.continue_stack = []
        self.jump_map = dict()
        self.transform_stmt(f.body())
        self.check_jump_linkes(self.jump_map)
        return self.stmts
    
    def transform_stmt(self,node):
        node.accept(self)
    
    def transform_expr(self,node):
        self.expr_nest_level += 1
        e = node.accept(self)
        self.expr_nest_level -= 1
        return e
    
    def is_statement(self):
        return self.expr_nest_level == 0
    
    def assign(self,loc,lhs,rhs):
        self.stmts.append(Assign(loc,self.address_of(lhs),rhs))
    
    def tmp_var(self,t):
        return self.scope_stack[-1].allocate_tmp(t)
    
    def label(self,label):
        self.stmts.append(LabelStmt(None,label))
    
    def jump(self,a1,a2=None):
        if a2 == None:
            self.stmts.append(Jump(None,a1))
        else :
            self.stmts.append(Jump(a1,a2))
    
    def cjump(self,loc,cond,thenlabel,elselabel):
        self.stmts.append(CJump(loc,cond,thenlabel,elselabel))
    
    def push_break(self,label):
        self.break_stack.append(label)
    
    def pop_break(self):
        if len(self.break_stack) == 0:
            raise Exception("unmatched push/pop for break stack")
        self.break_stack.pop()
    
    def current_break_target(self):
        if len(self.break_stack) == 0:
            raise JumpError("break from out of loop")
        return self.break_stack[-1]
    
    def push_continue(self,label):
        self.continue_stack.append(label)
    
    def pop_continue(self):
        if len(self.continue_stack) == 0:
            raise Exception("unmatched push/pop for continue stack")
        self.continue_stack.pop()

    def current_continue_target(self):
        if len(self.continue_stack) == 0:
            raise JumpError("continue from  out of loop")
        return self.continue_stack[-1]


    #
    # Helper methods for Visit
    #

    class JumpEntry:
        def __init__(self,label):
            self.label = label
            self.num_refered = 0
            self.is_defined = False
            self.location = None
    
    def define_label(self,name,loc):
        ent = self.get_jump_entry(name)
        if ent.is_defined:
            raise SemanticException("duplicated jump labels in "+name+"(): "+name)
        ent.is_defined = True
        ent.location = loc
        return ent.label
    
    def refer_label(self,name):
        ent = self.get_jump_entry(name)
        ent.num_refered += 1
        return ent.label
    
    def get_jump_entry(self,name):
        if name not in self.jump_map:
            ent = JumpEntry(Label())
            self.jump_map[name] = ent
        return self.jump_map[name]

    def check_jump_links(self,jmap):
        for labelname,jump in jmap.items():
            if not jump.is_defined:
                self.eh.error(jump.location(),
                    "undefined label: "+labelname)
            if jump.num_refered == 0:
                self.eh.warn(jump.location(),
                    "useless label: "+labelname)

    def transform_op_assign(self,loc,op,lhstype,lhs,rhs):
        if lhs.is_var():
            self.assign(loc,lhs,self.bin(op,lhstype,lhs,rhs))
            return None if self.is_statement() else lhs
        else :
            a = self.tmp_var(self.pointer_to(lhstype))
            self.assign(loc,self.ref(a),self.address_of(lhs))
            self.assign(loc,self.mem(a),self.bin(op,lhstype,self.mem(a),rhs))
            return None if self.is_statement() else self.mem(a)
    
    def bin(self,op,lefttype,left,right):
        if self.is_pointer_arithmetic(op,lefttype):
            return Bin(left.type(),op,left,
                    Bin(right.type(),Op.MUL,
                        right,self.ptr_base_size(lefttype)))
        else :
            return Bin(left.type(),op,left,right)
    
    # For multidimension array: t[e][d][c][b][a] ary;
    # &ary[a0][b0][c0][d0][e0]
    #     = &ary + edcb*a0 + edc*b0 + ed*c0 + e*d0 + e0
    #     = &ary + (((((a0)*b + b0)*c + c0)*d + d0)*e + e0) * sizeof(t)
    def transform_index(self,node):
        if node.is_multi_dimension():
            return Bin(self.int_t(),Op.ADD,
                    self.transform_expr(node.index()),
                    Bin(self.int_t(),Op.MUL,
                        Int(self.int_t(),node.length()),
                        self.transform_index(node.expr())))
        else :
            return self.transform_expr(node.index())


    #
    # Visit
    #

    def visit(self,node):
        #statements
        if isinstance(node,BlockNode):
            for var in node.variables():
                if var.has_initializer():
                    if var.is_private():
                        var.set_IR(self.transform_expr(var.initializer()))
                    else :
                        self.assign(var.location(),
                            self.ref(var),self.transform_expr(var.initializer()))
            for s in node.stmts():
                self.transform_stmt(s)
            self.scope_stack.pop()
            return None
        elif isinstance(node,ExprStmtNode):
            e = node.expr().accept(self)
            if e != None:
                self.eh.warn("useless expression",node.location())
            return None
        elif isinstance(node,IfNode):
            thenlabel = Label()
            elselabel = Label()
            endlabel = Label()
            cond = self.transform_expr(node.cond())
            if node.elsebody() == None:
                self.cjump(node.location(),cond,thenlabel,endlabel)
                self.label(thenlabel)
                self.transform_stmt(node.thenbody())
                self.label(endlabel)
            else :
                self.cjump(node.location(),cond,thenlabel,endlabel)
                self.label(thenlabel)
                self.transform_stmt(node.thenbody())
                self.jump(endlabel)
                self.label(elselabel)
                self.transform_stmt(node.elsebody())
                self.label(endlabel)
            return None
        elif isinstance(node,SwitchNode):
            cases = []
            endlabel = Label()
            defaultlabel = endlabel
            cond = self.transform_expr(node.cond())
            for c in node.cases():
                if c.is_default():
                    defaultlabel = c.label()
                else :
                    for val in c.values():
                        v = self.transform_expr(val)
                        cases.append(Case(v.value(),c.label()))
            self.stmts.append(Switch(node.location(),cond,cases,defaultlabel,endlabel))
            self.push_break(endlabel)
            for c in node.cases():
                self.label(c.label())
                self.transform_stmt(c.body())
            self.pop_break()
            self.label(endlabel)
            return None
        elif isinstance(node,CaseNode):
            raise Exception("must not happen")
        elif isinstance(node,WhileNode):
            beglabel = Label()
            bodylabel = Label()
            endlabel = Label()
            self.label(beglabel)
            self.cjump(node.location(),
                    self.transform_expr(node.cond()), bodylabel, endlabel)
            self.label(bodylabel)
            self.push_continue(beglabel)
            self.push_break(endlabel)
            self.transform_stmt(node.body())
            self.pop_break()
            self.pop_continue()
            self.jump(beglabel)
            self.label(endlabel)
            return None
        elif isinstance(node,DoWhileNode):
            beglabel = Label()
            contlabel = Label()
            endlabel = Label()
            self.push_continue(contlabel)
            self.push_break(endlabel)
            self.label(beglabel)
            self.transform_stmt(node.body())
            self.pop_break()
            self.pop_continue()
            self.label(contlabel)
            self.cjump(node.location(),self.transform_expr(node.cond()),beglabel,endlabel)
            self.label(endlabel)
            return None
        elif isinstance(node,ForNode):
            beglabel = Label()
            bodylabel = Label()
            contlabel = Label()
            endlabel = Label()
            self.transform_stmt(node.init())
            self.label(beglabel)
            self.cjump(node.location(),self.transform_expr(node.cond()),bodylabel,endlabel)
            self.label(bodylabel)
            self.push_continue(contlabel)
            self.push_break(endlabel)
            self.transform_stmt(node.body())
            self.pop_break()
            self.pop_continue()
            self.label(contlabel)
            self.transform_stmt(node.incr())
            self.jump(beglabel)
            self.label(endlabel)
            return None
        elif isinstance(node,BreakNode):
            try:
                self.jump(node.location(),self.current_break_target())
            except JumpError as ex:
                self.error(node,ex.message)
            return None
        elif isinstance(node,ContinueNode):
            try :
                self.jump(node.location(),self.current_continue_target())
            except JumpError as ex:
                self.error(node,ex.message)
            return None
        elif isinstance(node,GotoNode):
            self.jump(node.location(),self.refer_label(node.target()))
            return None
        elif isinstance(node,LabelNode):
            try:
                self.stmts.append(LabelStmt(node.location(),
                    self.define_label(node.name(),node.location())))
                if node.stmt() != None:
                    self.transform_stmt(node.stmt())
            except SemanticException as ex:
                self.error(node,ex.message)
            return None
        elif isinstance(node,ReturnNode):
            if node.expr() == None:
                self.stmts.append(Return(node.location(),None))
            else :
                self.stmts.append(Return(node.location(),self.transform_expr(node.expr())))
        #expressions  
        elif isinstance(node,CondExprNode):
            thenlabel = Label()
            elselabel = Label()
            endlabel = Label()
            var = self.tmp_var(node.type())
            cond = self.transform_expr(node.cond())
            self.cjump(node.location(),cond,thenlabel,elselabel)
            self.label(thenlabel)
            self.assign(node.then_expr().location(),
                self.ref(var),self.transform_expr(node.then_expr()))
            self.jump(endlabel)
            self.label(elselabel)
            self.assign(node.else_expr().location(),
                self.ref(var),self.transform_expr(node.else_expr()))
            self.jump(endlabel)
            self.label(endlabel)
            return None if self.is_statement() else self.ref(var)
        elif isinstance(node,LogicalOrNode):
            rightlabel = Label()
            endlabel = Label()
            var = self.tmp_var(node.type())
            self.assign(node.left().location(),
                self.ref(var),self.transform_expr(node.left()))
            self.cjump(node.location(),self.ref(var),rightlabel,endlabel)
            self.label(rightlabel)
            self.assign(node.right().location(),
                self.ref(var),self.transform_expr(node.right()))
            self.label(endlabel)
            return None if self.is_statement() else self.ref(var)
        elif isinstance(node,LogicalAndNode):
            rightlabel = Label()
            endlabel = Label()
            var = self.tmp_var(node.type())
            self.assign(node.left().location(),
                self.ref(var),self.transform_expr(node.left()))
            self.cjump(node.location(),self.ref(var),rightlabel,endlabel)
            self.label(rightlabel)
            self.assign(node.right().location(),
                self.ref(var),self.transform_expr(node.right()))
            self.label(endlabel)
            return None if self.is_statement() else self.ref(var)
        elif isinstance(node,AssignNode):
            lloc = node.lhs().location()
            rloc = node.rhs().location()
            if self.is_statement():
                rhs = self.transform_expr(node.rhs())
                self.assign(lloc,self.transform_expr(node.lhs()),rhs)
                return None
            else :
                #lhs = rhs  ->  tmp = rhs, lhs = tmp, tmp
                tmp = self.tmp_var(node.rhs().type())
                self.assign(rloc,self.ref(tmp),self.transform_expr(node.rhs()))
                self.assign(lloc,self.transform_expr(node.lhs()),self.ref(tmp))
                return self.ref(tmp)
        elif isinstance(node,OpAssignNode):
            rhs = self.transform_expr(node.rhs())
            lhs = self.transform_expr(node.lhs())
            t = node.lhs().type()
            op = Op.intern_binary(node.operator(),t.is_signed())
            return self.transform_op_assign(node.location(),op,t,lhs,rhs)
        elif isinstance(node,BinaryOpNode):
            right = self.transform_expr(node.right())
            left = self.transform_expr(node.left())
            op = Op.intern_binary(node.operator(),node.type().is_signed())
            t = node.type()
            r = node.right().type()
            l = node.left().type()
            if self.is_pointer_diff(op,l,r):
                tmp = Bin(self.asm_type(t),op,left,right)
                return Bin(self.asm_type(t),Op.S_DIV,tmp,self.ptr_base_size(l))
            elif self.is_pointer_arithmetic(op,l):
                tmp = Bin(self.asm_type(r),OP.MUL,right,self.ptr_base_size(l))
                return Bin(self.asm_type(t),op,left,tmp)
            elif self.is_pointer_arithmetic(op,r):
                tmp = Bin(self.asm_type(l),OP.MUL,left,self.ptr_base_size(r))
                return Bin(self.asm_type(t),op,tmp,right)
            else :
                return Bin(self.asm_type(t),op,left,right)
        elif isinstance(node,UnaryOpNode):
            if node.operator() == "+":
                return self.transform_expr(node.expr())
            else :
                return Uni(self.asm_type(node.type(),
                            Op.intern_unary(node.operator()),
                            self.transform_expr(node.expr())))
        elif isinstance(node,PrefixOpNode):
            t = node.expr().type()
            return self.transform_op_assign(node.location(),
                    self.bin_op(node.operator()),t,
                    self.transform_expr(node.expr()),self.imm(t,1))
        elif isinstance(node,SuffixOpNode):
            expr = self.transform_expr(node.expr())
            t = node.expr().type()
            op = self.bin_op(node.operator())
            loc = node.location()
            if self.is_statement():
                self.transform_op_assign(loc,op,t,expr,self.imm(t,1))
                return None
            elif expr.is_var():
                v = self.tmp_var(t)
                self.assign(loc,self.ref(v),expr)
                self.assign(loc,expr,self.bin(op,t,ref(v),self.imm(t,1)))
                return self.ref(v)
            else :
                a = self.tmp_var(self.pointer_to(t))
                v = self.tmp_var(t)
                self.assign(loc,self.ref(a),self.address_of(expr))
                self.assign(loc,self.ref(v),self.mem(a))
                self.assign(loc,self.mem(a),self.bin(op,t,self.mem(a),self.imm(t,1)))
        elif isinstance(node,FuncallNode):
            args = []
            for arg in reversed(node.args()):
                args.insert(0,self.transform_expr(arg))
            call = Call(self.asm_type(node.type()),
                self.transform_expr(node.expr()),args)
            if self.is_statement():
                self.stmts.append(ExprStmt(node.location(),call))
                return None
            else :
                tmp = self.tmp_var(node.type())
                self.assign(node.location(),self.ref(tmp),call)
                return self.ref(tmp)
        elif isinstance(node,ArefNode):
            expr = self.transform_expr(node.base_expr())
            offset = Bin(self.ptrdiff_t(),Op.MUL,self.size(node.element_size()),self.transform_index(node))
            addr = Bin(self.ptr_t(), Op.ADD, expr, offset)
            return self.mem(addr,node.type())
        elif isinstance(node,MemberNode):
            expr = self.address_of(self.transform_expr(node.expr()))
            offset = self.ptrdiff(node.offset())
            addr = Bin(self.ptr_t(),Op.ADD,expr,offset)
            if node.is_loadable():
                return self.mem(addr,node.type())
            else :
                return addr
        elif isinstance(node,PtrMemberNode):
            expr = self.transform_expr(node.expr())
            offset = self.ptrdiff(node.offset())
            addr = Bin(self.ptr_t(),Op.ADD,expr,offset)
            if node.is_loadable():
                return self.mem(addr,node.type())
            else :
                return addr
        elif isinstance(node,DereferenceNode):
            addr = self.transform_expr(node.expr())
            if node.is_loadable():
                return self.mem(addr,node.type())
            else :
                return addr
        elif isinstance(node,AddressNode):
            e = self.transform_expr(node.expr())
            if node.expr().is_loadable():
                return self.address_of(e)
            else :
                return e
        elif isinstance(node,CastNode):
            if node.is_effective_cast():
                if node.expr().type().is_signed():
                    return Uni(self.asm_type(node.type()),Op.S_CAST,self.transform_expr(node.expr()))
                else :
                    return Uni(self.asm_type(node.type()),Op.U_CAST,self.transform_expr(node.expr()))
            elif self.is_statement():
                self.transform_stmt(node.expr())
                return None
            else :
                return self.transform_expr(node.expr())
        elif isinstance(node,SizeofExprNode):
            return Int(self.size_t(),node.expr().alloc_size())
        elif isinstance(node,SizeofTypeNode):
            return Int(self.size_t(),node.operand().alloc_size())
        elif isinstance(node,VariableNode):
            if node.entity().is_constant():
                return self.transform_expr(node.entity().value())
            var = self.ref(node.entity())
            if node.is_loadable():
                return var
            else :
                return self.address_of(var)
        elif isinstance(node,IntegerLiteralNode):
            return Int(self.asm_type(node.type()),node.value())
        elif isinstance(node,StringLiteralNode):
            return Str(self.asm_type(node.type()),node.entry())
        else :
            raise Exception("unknown node in IRGenerator")
    # Visit end
        
    #
    # Utilities
    #

    def is_pointer_diff(self,op,l,r):
        return op == Op.SUB and l.is_pointer() and r.is_pointer()
    
    def is_pointer_arithmetic(self,op,optype):
        if op == Op.ADD or op == Op.SUB:
            return optype.is_pointer()
        else :
            return False
    
    def ptr_base_size(self,t):
        return Int(self.ptrdiff_t(),t.base_type().size())
    
    def bin_op(self,uni):
        return Op.ADD if uni == "++" else Op.SUB

    def address_of(self,expr):
        return expr.address_node(self.ptr_t())
    
    def ref(self,ent):
        return Var(self.var_type(ent.type()),ent)
    
    def mem(self,expr,t=None):
        if t == None:
            return Mem(self.asm_type(expr.type().base_type()),self.ref(ent))
        else :
            return Mem(self.asm_type(t),expr)
    
    def ptrdiff(self,n):
        return Int(self.ptrdiff_t(),n)
    
    def size(self,n):
        return Int(self.size_t(),n)
    
    def imm(self,optype,n):
        if optype.is_pointer():
            return Int(self.ptrdiff_t(),n)
        else :
            return Int(self.int_t(),n)
    
    def pointer_to(self,t):
        return self.ttable.pointer_to(t)
    
    def asm_type(self,t):
        if t.is_void():
            return self.int_t()
        return asm.Type.get(t.size())

    def var_type(self,t):
        if not t.is_scalar():
            return None
        return asm.Type.get(t.size())
    
    def int_t(self):
        return asm.Type.get(self.ttable.int_size())
    def size_t(self):
        return asm.Type.get(self.ttable.long_size())
    def ptr_t(self):
        return asm.Type.get(self.ttable.pointer_size())
    def ptrdiff_t(self):
        return asm.Type.get(self.ttable.long_size())
    
    def error(self,n,msg):
        self.eh.error(msg,n.location())