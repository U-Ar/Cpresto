from abst.AddressNode import *
from abst.ArefNode import *
from abst.AssignNode import *
from abst.AST import *
from abst.ASTVisitor import ASTVisitor
from abst.BinaryOpNode import *
from abst.BlockNode import *
from abst.BreakNode import *
from abst.CaseNode import *
from abst.CastNode import *
from abst.CprestoToken import *
from abst.CompositeTypeDefinition import *
from abst.CondExprNode import *
from abst.ContinueNode import *
from abst.Declarations import *
from abst.DeclarationVisitor import *
from abst.DereferenceNode import *
from abst.DoWhileNode import *
from abst.Dumpable import Dumpable
from abst.Dumper import *
from abst.ExprNode import *
from abst.ExprStmtNode import *
from abst.ForNode import *
from abst.FuncallNode import *
from abst.GotoNode import *
from abst.IfNode import *
from abst.IntegerLiteralNode import *
from abst.LabelNode import *
from abst.LHSNode import *
from abst.LiteralNode import *
from abst.Location import *
from abst.LogicalAndNode import *
from abst.LogicalOrNode import *
from abst.MemberNode import *
from abst.Node import *
from abst.OpAssignNode import *
from abst.PrefixOpNode import *
from abst.PtrMemberNode import *
from abst.ReturnNode import *
from abst.SizeofExprNode import *
from abst.SizeofTypeNode import *
from abst.Slot import *
from abst.StmtNode import *
from abst.StringLiteralNode import *
from abst.StructNode import *
from abst.SuffixOpNode import *
from abst.SwitchNode import *
from abst.TypeDefinition import *
from abst.TypedefNode import *
from abst.TypeNode import *
from abst.UnaryArithmeticOpNode import *
from abst.UnaryOpNode import *
from abst.UnionNode import *
from abst.VariableNode import *
from abst.WhileNode import *

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
