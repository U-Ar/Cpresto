from asm.Label import Label
from type.Type import Type
from type.TypeTable import TypeTable
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
        #expressions  ###############bookmark
        elif isinstance(node,CondExprNode):
            self.visit_expr(node.cond())
            self.visit_expr(node.then_expr())
            if node.else_expr() != None:
                self.visit_expr(node.else_expr())
        elif isinstance(node,LogicalOrNode):
            self.visit_expr(node.left())
            self.visit_expr(node.right())
        elif isinstance(node,LogicalAndNode):
            self.visit_expr(node.left())
            self.visit_expr(node.right())
        elif isinstance(node,AssignNode):
            self.visit_expr(node.lhs())
            self.visit_expr(node.rhs())
        elif isinstance(node,OpAssignNode):
            self.visit_expr(node.lhs())
            self.visit_expr(node.rhs())
        elif isinstance(node,BinaryOpNode):
            self.visit_expr(node.left())
            self.visit_expr(node.right())
        elif isinstance(node,UnaryOpNode):
            self.visit_expr(node.expr())
        elif isinstance(node,PrefixOpNode):
            self.visit_expr(node.expr())
        elif isinstance(node,SuffixOpNode):
            self.visit_expr(node.expr())
        elif isinstance(node,FuncallNode):
            self.visit_expr(node.expr())
            self.visit_exprs(node.args())
        elif isinstance(node,ArefNode):
            self.visit_expr(node.expr())
            self.visit_expr(node.index())
        elif isinstance(node,MemberNode):
            self.visit_expr(node.expr())
        elif isinstance(node,PtrMemberNode):
            self.visit_expr(node.expr())
        elif isinstance(node,DereferenceNode):
            self.visit_expr(node.expr())
        elif isinstance(node,AddressNode):
            self.visit_expr(node.expr())
        elif isinstance(node,CastNode):
            self.visit_expr(node.expr())
        elif isinstance(node,SizeofExprNode):
            self.visit_expr(node.expr())
        elif isinstance(node,SizeofTypeNode):
            return None
        elif isinstance(node,VariableNode):
            return None
        elif isinstance(node,IntegerLiteralNode):
            return None
        elif isinstance(node,StringLiteralNode):
            return None

        return None

    
