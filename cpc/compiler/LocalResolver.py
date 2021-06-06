from entity.ConstantTable import ConstantTable
from entity.TopLevelScope import TopLevelScope
from entity.LocalScope import LocalScope

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

from exception.SemanticException import SemanticException
from .Visitor import Visitor

class LocalResolver(Visitor):
    def __init__(self,h):
        self.error_handler = h
        self.scope_stack = []
        self.constant_table = ConstantTable()
    
    def resolve(self,n):
        if isinstance(n,AST):
            toplevel = TopLevelScope()
            self.scope_stack.append(toplevel)
            for decl in n.declarations():
                toplevel.declare_entity(decl)
            for ent in n.definitions():
                toplevel.define_entity(ent)
            
            self.resolve_gvar_initializers(n.defined_variables())
            self.resolve_constant_values(n.constants())
            self.resolve_functions(n.defined_functions())

            toplevel.check_references(self.error_handler)
            if self.error_handler.error_occured():
                raise SemanticException("compile failed.")

            n.set_scope(toplevel)
            n.set_constant_table(self.constant_table)

        elif isinstance(n,StmtNode) or isinstance(n,ExprNode):
            n.accept(self)
    
    def resolve_gvar_initializers(self,gvars):
        for gvar in gvars:
            if gvar.has_initializer():
                self.resolve(gvar.initializer())
    
    def resolve_constant_values(self,consts):
        for c in consts:
            self.resolve(c.value())

    def resolve_functions(self,funcs):
        for fun in funcs:
            self.push_scope(fun.parameters())
            self.resolve(fun.body())
            fun.set_scope(self.pop_scope())
    
    def push_scope(self,vars):
        scope = LocalScope(self.current_scope())
        for v in vars:
            if scope.is_defined_locally(v.name()):
                self.error(v.location(),"duplicated variable in scope: "+v.name())
            else :
                scope.define_variable(v)
        self.scope_stack.append(scope)

    def pop_scope(self):
        return self.scope_stack.pop()
    
    def current_scope(self):
        return self.scope_stack[-1]
    
    def error(self,node,message):
        if isinstance(node,Location):
            self.error_handler.error(message,node)
        else:
            self.error_handler.error(message,node.location())

    #changed: BlockNode, StringLiteralNode, VariableNode
    def visit(self,node):
        if isinstance(node,BlockNode):
            self.push_scope(node.variables())
            super().visit(node)
            node.set_scope(self.pop_scope())
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
            try:
                ent = self.current_scope().get(node.name())
                ent.refered()
                node.set_entity(ent)
            except SemanticException as ex:
                self.error(node,ex.message)
            return None
        elif isinstance(node,IntegerLiteralNode):
            return None
        elif isinstance(node,StringLiteralNode):
            node.set_entry(self.constant_table.intern(node.value()))
            return None

        return None