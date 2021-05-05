from ..ast.AbstractAssignNode import *
from ..ast.AdressNode import *
from ..ast.ArefNode import *
from ..ast.AssignNode import *
from ..ast.AST import *
from ..ast.ASTVisitor import *
from ..ast.BinaryOpNode import *
from ..ast.BlockNode import *
from ..ast.BreakNode import *
from ..ast.CaseNode import *
from ..ast.CastNode import *
from ..ast.CflatToken import *
from ..ast.CompositeTypeDefinition import *
from ..ast.CondExprNode import *
from ..ast.ContinueNode import *
from ..ast.Declarations import *
from ..ast.DeclarationVisitor import *
from ..ast.DereferenceNode import *
from ..ast.DoWhileNode import *
from ..ast.Dumpable import *
from ..ast.Dumper import *
from ..ast.ExprNode import *
from ..ast.ExprStmtNode import *
from ..ast.ForNode import *
from ..ast.FuncallNode import *
from ..ast.GotoNode import *
from ..ast.IfNode import *
from ..ast.IntegerLiteralNode import *
from ..ast.LabelNode import *
from ..ast.LHSNode import *
from ..ast.LiteralNode import *
from ..ast.Location import *
from ..ast.LogicalAndNode import *
from ..ast.LogicalOrNode import *
from ..ast.MemberNode import *
from ..ast.Node import *
from ..ast.OpAssignNode import *
from ..ast.PrefixOpNode import *
from ..ast.PtrMemberNode import *
from ..ast.ReturnNode import *
from ..ast.SizeofExprNode import *
from ..ast.SizeofTypeNode import *
from ..ast.Slot import *
from ..ast.StmtNode import *
from ..ast.StringLiteralNode import *
from ..ast.StructNode import *
from ..ast.SuffixOpNode import *
from ..ast.SwitchNode import *
from ..ast.TypeDefinition import *
from ..ast.TypedefNode import *
from ..ast.TypeNode import *
from ..ast.UnaryArithmeticOpNode import *
from ..ast.UnaryOpNode import *
from ..ast.UnionNode import *
from ..ast.VariableNode import *
from ..ast.WhileNode import *

from ..exception.SemanticException import SemanticException
from ..exception.SemanticError import SemanticError
from Visitor import Visitor

class DereferenceChecker(Visitor):
    def __init__(self,type_table,h):
        self.type_table = type_table
        self.error_handler = h

    #
    # checker
    #
    
    def check(self, ast):
        for v in ast.defined_variables():
            self.check_toplevel_variable(v)
        for f in ast.defined_functions():
            self.check(f.body())
        if self.error_handler.error_occured():
            raise SemanticException("compile failed.")
    
    def check_toplevel_variable(self,var):
        self.check_variable(var)
        if var.has_initializer():
            self.check_constant(var.initializer())

    def check_constant(self,expr):
        if not expr.is_constant():
            self.error_handler.error("not a constant", expr.location())
    
    def check(self,node):
        if isinstance(node,StmtNode):
            node.accept(self)
        elif isinstance(node,ExprNode):
            node.accept(self)
    
    def check_variable(self,var):
        if var.has_initializer():
            try:
                self.check(var.initializer())
            except SemanticError as ex:
                pass
    
    def check_assignment(self,node):
        if not node.lhs().is_assignable():
            self.semantic_error("invalid lhs expression", node.location())
    
    def check_member_ref(self,loc,t,memb):
        if not t.is_composite_type():
            self.semantic_error("accessing member `"+memb+"` for non-struct/union: "+t,loc)
        t = t.get_composite_type()
        if not t.has_member(memb):
            self.semantic_error(t.to_string()+" does not have member: "+memb, loc)
        
    #
    # Utilities
    #
    def handle_implicit_address(self,node):
        if not node.is_loadable():
            t = node.type()
            if t.is_array():
                # int[4] ary; ary; shold generate int*
                node.set_type(self.type_table.pointer_to(t.base_type()))
            else :
                node.set_type(self.type_table.pointer_to(t))

    def undereferable_error(self,loc):
        self.semantic_error("dereferencing non-pointer expression",loc)
    
    def semantic_error(self,msg,node):
        if isinstance(node,Node):
            self.semantic_error(msg,node.location())
        else :
            self.error_handler.error(msg,node)
            raise SemanticError("invalid expr")

    #
    # visit
    #

    #changed: BlockNode, AssignNode, OpAssignNode, PrefixOpNode,
    #         SuffixOpNode, FuncallNode, ArefNode, MemberNode,
    #         PtrMemberNode, DereferenceNode, AddressNode,
    #         VariableNode, CastNode
    def visit(self,node):
        #statements
        if isinstance(node,BlockNode):
            for var in node.variables():
                self.check_variable(var)
            for stmt in node.stmts():
                try:
                    self.check(stmt)
                except SemanticError as ex:
                    pass
            return None
        elif isinstance(node,ExprStmtNode):
            self.visit_expr(node.expr())
        elif isinstance(node,IfNode):
            self.visit_expr(node.cond())
            self.visit_stmt(node.then_body())
            if node.else_body() != None:
                self.visit_stmt(node.else_body())
        elif isinstance(node,SwitchNode):
            self.visit_expr(node.cond())
            self.visit_stmts(node.cases())
        elif isinstance(node,CaseNode):
            self.visit_exprs(node.values())
            self.visit_stmt(node.body())
        elif isinstance(node,WhileNode):
            self.visit_expr(node.cond())
            self.visit_stmt(node.body())
        elif isinstance(node,DoWhileNode):
            self.visit_stmt(node.body())
            self.visit_expr(node.cond())
        elif isinstance(node,ForNode):
            self.visit_stmt(node.init())
            self.visit_expr(node.cond())
            self.visit_stmt(node.incr())
            self.visit_stmt(node.body())
        elif isinstance(node,BreakNode) or \
            isinstance(node,ContinueNode) or \
                isinstance(node,GotoNode):
            return None
        elif isinstance(node,LabelNode):
            self.visit_stmt(node.stmt())
        elif isinstance(node,ReturnNode):
            if node.expr() != None:
                self.visit_expr(node.expr())
        #expressions
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
            super().visit(node)
            self.check_assignment(node)
            return None
        elif isinstance(node,OpAssignNode):
            super().visit(node)
            self.check_assignment(node)
            return None
        elif isinstance(node,BinaryOpNode):
            self.visit_expr(node.left())
            self.visit_expr(node.right())
        elif isinstance(node,UnaryOpNode):
            self.visit_expr(node.expr())
        elif isinstance(node,PrefixOpNode):
            super().visit(node)
            if not node.expr().is_assignable():
                self.semantic_error("cannot increment/decrement",node.expr().location())
            return None
        elif isinstance(node,SuffixOpNode):
            super().visit(node)
            if not node.expr().is_assignable():
                self.semantic_error("cannot increment/decrement",node.expr().location())
            return None
        elif isinstance(node,FuncallNode):
            super().visit(node)
            if not node.expr().is_callable():
                self.semantic_error("calling object is not a function",node.expr().location())
            return None
        elif isinstance(node,ArefNode):
            super().visit(node)
            if not node.expr().is_pointer():
                self.semantic_error("indexing non-array/pointer expression",node.expr().location())
            self.handle_implicit_address(node)
            return None
        elif isinstance(node,MemberNode):
            super().visit(node)
            self.check_member_ref(node.location(),node.expr().type(),node.member())
            self.handle_implicit_address(node)
            return None
        elif isinstance(node,PtrMemberNode):
            super().visit(node)
            if not node.expr().is_pointer():
                self.undereferable_error(node.location())
            self.check_member_ref(node.location(),node.derefered_type(),node.member())
            self.handle_implicit_address(node)
            return None
        elif isinstance(node,DereferenceNode):
            super().visit(node)
            if not node.expr().is_pointer():
                self.undereferable_error(node.location())
            self.handle_implicit_address(node)
            return None
        elif isinstance(node,AddressNode):
            super().visit(node)
            if not node.expr().is_lvalue():
                self.semantic_error("invalid expression for &",node.location())
            base = node.expr().type()
            if not node.expr().is_loadable():
                node.set_type(base)
            else :
                node.set_type(self.type_table.pointer_to(base))
            return None
        elif isinstance(node,CastNode):
            super().visit(node)
            if node.type().is_array():
                self.semantic_error("cast specifies array type",node.location())
            return None
        elif isinstance(node,SizeofExprNode):
            self.visit_expr(node.expr())
        elif isinstance(node,SizeofTypeNode):
            return None
        elif isinstance(node,VariableNode):
            super().visit(node)
            if node.entity().is_constant():
                self.check_constant(node.entity().value())
            self.handle_implicit_address(node)
            return None
        elif isinstance(node,IntegerLiteralNode):
            return None
        elif isinstance(node,StringLiteralNode):
            return None

        return None