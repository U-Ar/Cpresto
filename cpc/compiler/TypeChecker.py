import abst
import entity
import type
from utils.ErrorHandler import ErrorHandler
import exception
from .Visitor import Visitor

class TypeChecker(Visitor):
    def __init__(self,type_table,error_handler):
        self.ttable = type_table
        self.eh = error_handler
        self.current_function = None
    
    def check(self,node):
        if isinstance(node,StmtNode):
            self.visit_stmt(node)
        elif isinstance(node,ExprNode):
            self.visit_expr(node)
        elif isinstance(node,AST):
            ast = node
            for var in ast.defined_variables():
                self.check_variable(var)
            for f in ast.defined_funtions():
                self.current_function = f
                self.check_return_type(f)
                self.check_param_types(f)
                self.check(f.body())
            if self.eh.error_occured():
                raise SemanticException("compile failed.")
    
    def check_return_type(self,f):
        if self.is_invalid_return_type(f.return_type()):
            self.error(f.location(),"returns invalid type: "+f.return_type().to_string())
    
    def check_param_types(self,f):
        for param in f.parameters():
            if self.is_invalid_parameter_type(param.type()):
                self.error(param.location(),"invalid parameter type: " + param.to_string())
    
    ## Helper methods for visit

    def check_variable(self,var):
        if self.is_invalid_variable_type(var.type()):
            self.error(var.location(),"invalid variable type")
            return 
        if var.has_initializer():
            if self.is_invalid_LHS_type(var.type()):
                self.error(var.location(), "invalid LHS type: " + var.type())
                return 
            self.check(var.initializer())
            var.set_initializer(self.implicit_cast(var.type(),var.initializer()))

    def check_cond(self,cond):
        self.must_be_scalar(cond,"condition expression")
    
    def is_safe_integer_cast(self,node,t):
        if not t.is_integer():
            return False
        if not isinstance(node,IntegerLiteralNode):
            return False
        return t.is_in_domain(node.value())

    def check_LHS(self,lhs):
        if lhs.is_parameter():
            return True
        elif self.is_invalid_LHS_type(lhs.type()):
            self.error(lhs,"invalid LHS expression type: " + lhs.type())
            return False
        return True
    
    def expects_same_integer_or_pointer_diff(self,node):
        if node.left().is_pointer() and node.right().is_pointer():
            if node.operator() == "+":
                self.error(node,"invalid operation: pointer + pointer")
                return 
            node.set_type(self.ttable.ptr_diff_type())
        elif node.left().is_pointer():
            self.must_be_integer(node.right(),node.operator())
            # promote integer for pointer calculation
            node.set_right(self.integral_promoted_expr(node.right()))
            node.set_type(node.left().type())
        elif node.right().is_pointer():
            if node.operator() == "-":
                self.error(node,"invalid operation: integer - pointer")
                return 
            self.must_be_integer(node.left(),node.operator())
            # promote integer for pointer calculation
            node.set_left(self.integral_promoted_expr(node.left()))
            node.set_type(node.right().type())
        else :
            self.expects_same_integer(node)

    
    def integral_promoted_expr(self,expr):
        t = self.integral_promotion(expr.type())
        if t.is_same_type(expr.type()):
            return expr
        else :
            return CastNode(t,expr)

    def expects_same_integer(self,node):
        if not self.must_be_integer(node.left(),node.operator()):
            return
        if not self.must_be_integer(node.right(),node.operator()):
            return
        self.arighmetic_implicit_cast(node)
    
    def expects_comparable_scalars(self,node):
        if not self.must_be_scalar(node.left(),node.operator()):
            return
        if not self.must_be_scalar(node.right(),node.operator()):
            return
        if node.left().type().is_pointer():
            right = self.force_pointer_type(node.left(),node.right())
            node.set_right(right)
            node.set_type(node.left().type())
            return 
        if node.right().type().is_pointer():
            left = self.force_pointer_type(node.right(),node.right())
            node.set_left(left)
            node.set_type(node.right().type())
            return
        self.arithmetic_implicit_cast(node)

    def force_pointer_type(self,master,slave):
        if master.type().is_compatible(slave.type()):
            return slave
        else :
            self.warn(slave, "incompatible implicit cast from " \
                + slave.type().to_string() + " to " + master.type().to_string())
            return CastNode(master.type(),slave)
    
    def arithmetic_implicit_cast(self,node):
        r = self.integral_promotion(node.right().type())
        l = self.integral_promotion(node.left().type())
        target = self.usual_arithmetic_conversion(l,r)
        if not l.is_same_type(target):
            node.set_left(CastNode(target,node.left()))
        if not r.is_same_type(target):
            node.set_right(CastNode(target,node.right()))
        node.set_type(target)
    
    def expects_scalar_LHS(self,node):
        if node.expr().is_parameter():
            pass # parameter is always a scalar
        elif node.expr().type().is_array():
            self.wrong_type_error(node.expr(),node.operator())
            return
        else :
            self.must_be_scalar(node.expr(),node.operator())
        if node.expr().type().is_integer():
            op_type = self.integral_promotion(node.expr().type())
            if not node.expr().type().is_same_type(op_type):
                node.set_op_type(op_type)
            node.set_amount(1)
        elif node.expr().type().is_pointer():
            if node.expr().type().base_type().is_void():
                self.wrong_type_error(node.expr(),node.operator())
                return
            node.set_amount(node.expr().type().base_type().size())
        else :
            raise Exception("must not happen")
    
    def cast_optional_arg(self, arg):
        if not arg.type().is_integer():
            return arg
        t = self.ttable.signed_stack_type() if arg.type().is_signed() \
            else self.ttable.unsigned_stack_type()
        if arg.type().size() < t.size():
            return self.implicit_cast(t,arg)
        else :
            return arg

    ## Visit

    def visit(self,node):
        #statements
        if isinstance(node,BlockNode):
            for var in node.variables():
                self.check_variable(var)
            for n in node.stmts():
                self.check(n)
            return None
        elif isinstance(node,ExprStmtNode):
            self.check(node.expr())
            if self.is_invalid_statement_type(node.expr().type()):
                self.error(node,"invalid statement type: " + node.expr().type().to_string())
            return None
        elif isinstance(node,IfNode):
            super().visit(node)
            self.check_cond(node.cond())
            return None
        elif isinstance(node,WhileNode):
            super().visit(node)
            self.check_cond(node.cond())
            return None
        elif isinstance(node,ForNode):
            super().visit(node)
            self.check_cond(node.cond())
            return None
        elif isinstance(node,SwitchNode):
            super().visit(node)
            self.must_be_integer(node.cond(),"condition expression")
            return None
        elif isinstance(node,ReturnNode):
            super().visit(node)
            if self.current_function.is_void():
                if node.expr() != None:
                    self.error(node,"returning value from void function")
            else :
                if node.expr() == None:
                    self.error(node,"missing return value")
                    return None
                elif node.expr().type().is_void():
                    self.error(node,"returning void")
                    return None
                node.set_expr(self.implicit_cast( \
                    self.current_function.return_type(),node.expr()))
            return None
        # Assignments
        elif isinstance(node,AssignNode):
            super().visit(node)
            if not check_LHS(node.lhs()) or not check_RHS(node.rhs()):
                return None
            node.set_RHS(self.implicit_cast(node.lhs().type(),node.rhs()))
            return None
        elif isinstance(node,OpAssignNode):
            super().visit(node)
            if not check_LHS(node.lhs()) or not check_RHS(node.rhs()):
                return None
            if node.operator() == "+" or node.operator() == "-":
                if node.lhs().type().is_pointer():
                    self.must_be_integer(node.rhs(),node.operator())
                    node.set_RHS(self.integral_promoted_expr(node.rhs()))
                    return None
            if not self.must_be_integer(node.lhs(),node.operator()) or \
                not self.must_be_integer(node.rhs(),node.operator()):
                return None
            l = self.integral_promotion(node.lhs().type())
            r = self.integral_promotion(node.rhs().type())
            op_type = self.usual_arithmetic_conversion(l,r)
            if not op_type.is_compatible(l) and \
              not self.is_safe_integer_cast(node.rhs(),op_type):
                self.warn(node,"incompatible implicit cast from " \
                    + op_type.to_string() + " to " + l.to_string())
            if not r.is_same_type(op_type):
                node.set_RHS(CastNode(op_type,node.rhs()))
            return None
        elif isinstance(node,BinaryOpNode):
            super().visit(node)
            if node.operator() == "+" or node.operator() == "-":
                self.expects_same_integer_or_pointer_diff(node)
            elif node.operator() == "*" or \
                 node.operator() == "/" or \
                 node.operator() == "%" or \
                 node.operator() == "&" or \
                 node.operator() == "|" or \
                 node.operator() == "^" or \
                 node.operator() == "<<" or \
                 node.operator() == ">>" :
                self.expects_same_integer(node)
            elif node.operator() == "==" or \
                 node.operator() == "!=" or \
                 node.operator() == "<" or \
                 node.operator() == "<=" or \
                 node.operator() == ">" or \
                 node.operator() == ">=":
                self.expects_comparable_scalars(node)
            else :
                raise Exception("unknown binary operator: " + node.operator())
            return None
        elif isinstance(node,LogicalAndNode):
            super().visit(node)
            self.expects_comparable_scalars(node)
            return None
        elif isinstance(node,LogicalOrNode):
            super().visit(node)
            self.expects_comparable_scalars(node)
            return None
        elif isinstance(node,UnaryOpNode):
            super().visit(node)
            if node.operator() == "!":
                self.must_be_scalar(node.expr(),node.operator())
            else :
                self.must_be_integer(node.expr(),node.operator())
            return None
        elif isinstance(node,PrefixOpNode):
            super().visit(node)
            self.expects_scalar_LHS(node)
            return None
        elif isinstance(node,SuffixOpNode):
            super().visit(node)
            self.expects_scalar_LHS(node)
            return None
        # for EXPR(ARG), checks
        # - The number of argument matches function prototype
        # - ARG matches function prototype
        # - ARG is neither a struct nor an union
        elif isinstance(node,FuncallNode):
            super().visit(node)
            t = node.function_type()
            if not t.accepts_argc(node.num_args()):
                self.error(node,"wrong number of arguments: " + str(node.num_args))
                return None
            newargs = []
            args = iter(node.args())
            for param in t.param_types():
                arg = next(args)
                newargs.append(self.implicit_cast(param,arg)  \
                    if self.check_RHS(arg) else arg)
            # optional args
            while True:
                arg = next(args,None)
                if arg == None:
                    break
                newargs.append(self.cast_optional_arg(arg) \
                    if self.check_RHS(arg) else arg)
            node.replace_args(newargs)
            return None
        elif isinstance(node,ArefNode):
            super().visit(node)
            self.must_be_integer(node.index(),"[]")
            return None
        elif isinstance(node,CastNode):
            super().visit(node)
            if not node.expr().type().is_castable_to(node.type()):
                self.invalid_cast_error(node,node.expr().type(),node.type())
            return None
        elif isinstance(node,CaseNode):
            self.visit_exprs(node.values())
            self.visit_stmt(node.body())
        elif isinstance(node,DoWhileNode):
            self.visit_stmt(node.body())
            self.visit_expr(node.cond())
        elif isinstance(node,BreakNode) or \
            isinstance(node,ContinueNode) or \
                isinstance(node,GotoNode):
            return None
        elif isinstance(node,LabelNode):
            self.visit_stmt(node.stmt())
        elif isinstance(node,CondExprNode):
            self.visit_expr(node.cond())
            self.visit_expr(node.then_expr())
            if node.else_expr() != None:
                self.visit_expr(node.else_expr())
        elif isinstance(node,MemberNode):
            self.visit_expr(node.expr())
        elif isinstance(node,PtrMemberNode):
            self.visit_expr(node.expr())
        elif isinstance(node,DereferenceNode):
            self.visit_expr(node.expr())
        elif isinstance(node,AddressNode):
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
        else :
            raise Exception("TypeChecker found unknown node.")


    ## Utilities

    def check_RHS(self,rhs):
        if self.is_invalid_RHS_type(rhs.type()):
            self.error(rhs, "invalid RHS expression type: " + rhs.type())
            return False
        return True

    # processes forced-implicit-cast
    # applied to: return expr, assignment RHS, funcall argument
    def implicit_cast(self,target_type,expr):
        if expr.type().is_same_type(target_type):
            return expr
        elif expr.type().is_castable_to(target_type):
            if not expr.type().is_compatible(target_type) \
            and not is_safe_integer_cast(expr,target_type):
                self.warn(expr,"incompatible implicit cast from " \
                    + expr.type().to_string() + " to " + target_type.to_string()) 
            return CastNode(target_type,expr)
        else :
            self.invalid_cast_error(expr,expr.type(),target_type)
            return expr

    #process integral promotion (integers only)
    def integral_promotion(self,t):
        if not t.is_integer():
            raise Exception("integral_promotion for "+t.to_string())
        int_type = self.ttable.signed_int()
        if t.size() < int_type.size():
            return int_type
        else :
            return t

    #usual arithmetic conversion for ILP32 platform
    def usual_arithmetic_conversion(self,l,r):
        s_int = self.ttable.signed_int()
        u_int = self.ttable.unsigned_int()
        s_long = self.ttable.signed_long()
        u_long = self.ttable.unsigned_long()
        if (l.is_same_type(u_int) and r.is_same_type(s_long)) \
            (r.is_same_type(u_int) and l.is_same_type(s_long)):
            return u_long
        elif l.is_same_type(u_long) or r.is_same_type(u_long):
            return u_long
        elif l.is_same_type(s_long) or r.is_same_type(s_long):
            return s_long
        elif l.is_same_type(u_int) or r.is_same_type(u_int):
            return u_int
        else :
            return s_int
    
    def is_invalid_statement_type(self,t):
        return t.is_struct() or t.is_union()
    
    def is_invalid_return_type(self,t):
        return t.is_struct() or t.is_union() or t.is_array()
    
    def is_invalid_parameter_type(self,t):
        return t.is_struct() or t.is_union() or t.is_void() or \
            t.is_incomplete_array()
    
    def is_invalid_variable_type(self,t):
        return t.is_void() or (t.is_array() and not t.is_allocated_array())
    
    def is_invalid_LHS_type(self,t):
        return t.is_struct() or t.is_union() or t.is_array() or t.is_void()
    
    def is_invalid_RHS_type(self,t):
        return t.is_struct() or t.is_union() or t.is_void()
    
    def must_be_integer(self,expr,op):
        if not expr.type().is_integer():
            self.wrong_type_error(expr,op)
            return False
        return True
    
    def must_be_scalar(self,expr,op):
        if not expr.type().is_scalar():
            self.wrong_type_error(expr,op)
            return False
        return True

    ## error handling

    def invalid_cast_error(self,n,l,r):
        self.error(n,"invalid cast from " + l.to_string() + " to " + r.to_string())
    
    def wrong_type_error(self,expr,op):
        self.error(expr,"wrong operand type for " + op + " to " + expr.type().to_string())
    
    def warn(self,n,msg):
        self.eh.warn(msg,n.location())
    
    def error(self,n,msg):
        if isinstance(n,Node):
            self.eh.error(msg,n.location())
        else :
            self.eh.error(msg,n)



