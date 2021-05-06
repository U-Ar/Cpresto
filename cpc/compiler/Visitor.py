from ..ast.ASTVisitor import ASTVisitor

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

class Visitor(ASTVisitor):
    def __init__(self):
        pass

    def visit_stmt(self,stmt):
        stmt.accept(self)
    
    def visit_stmts(self,stmts):
        for s in stmts:
            self.visit_stmt(s)
    
    def visit_expr(self,expr):
        expr.accept(self)
    
    def visit_exprs(self,exprs):
        for e in exprs:
            self.visit_expr(e)
    

    
    def visit(self,node):
        #statements
        if isinstance(node,BlockNode):
            for v in node.variables():
                if v.has_initializer():
                    self.visit_expr(v.initializer())
            self.visit_stmts(node.stmts())
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
