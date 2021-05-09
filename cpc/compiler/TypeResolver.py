from abst.AbstractAssignNode import *
from abst.AddressNode import *
from abst.ArefNode import *
from abst.AssignNode import *
from abst.AST import *
from abst.ASTVisitor import *
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
from abst.Dumpable import *
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
#added:   StructNode, UnionNode, TypedefNode, 
#         DefinedVariable, UndefinedVariable, Constant,
#         DefinedFunction, Undefinedfunction
from entity.DefinedVariable import DefinedVariable
from entity.UndefinedVariable import UndefinedVariable
from entity.Constant import Constant
from entity.DefinedFunction import DefinedFunction
from entity.UndefinedFunction import UndefinedFunction

from exception.SemanticException import SemanticException
from .Visitor import Visitor

class TypeResolver(Visitor):
    def __init__(self,type_table,error_handler):
        self.type_table = type_table
        self.error_handler = error_handler
    
    def resolve(self,ast):
        self.define_types(ast.types())
        for t in ast.types():
            t.accept(self)
        for e in ast.entities():
            e.accept(self)
    
    def define_types(self,deftypes):
        for d in deftypes:
            if self.type_table.is_defined(d.type_ref()):
                self.error("dumplicated type definition: "+d.type_ref(),d)
            else:
                self.type_table.put(d.type_ref(),d.defining_type())
    
    def bind_type(self,n):
        if n.is_resolved():
            return 
        n.set_type(self.type_table.get(n.type_ref()))

    def resolve_composite_type(self,d):
        ct = self.type_table.get(d.type_node().type_ref())
        if ct == None:
            raise Exception("cannot intern struct/union: "+d.name())
        for s in ct.members():
            self.bind_type(s.type_node())
    
    def resolve_function_header(self,func):
        self.bind_type(func.type_node())
        for param in func.parameters():
            t = self.type_table.get_param_type(param.type_node().type_ref())
            param.type_node().set_type(t)
    
    def error(self,msg,node):
        self.error_handler.error(msg,node.location())


    #added  : StructNode, UnionNode, TypedefNode, 
    #         DefinedVariable, UndefinedVariable, Constant,
    #         DefinedFunction, Undefinedfunction
    #changed: BlockNode, CastNode, SizeofExprNode, 
    #         SizeofTypeNode, IntegerLiteralNode, StringLiteralNode
    
    def visit(self,node):
        #entities
        if isinstance(node,DefinedVariable):
            self.bind_type(node.type_node())
            if node.has_initializer():
                self.visit_expr(node.initializer())
            return None
        elif isinstance(node,UndefinedVariable):
            self.bind_type(node.type_node())
            return None
        elif isinstance(node,Constant):
            self.bind_type(node.type_node())
            self.visit_expr(node.value())
            return None
        elif isinstance(node,DefinedFunction):
            self.resolve_function_header(node)
            self.visit_stmt(node.body())
            return None
        elif isinstance(node,UndefinedFunction):
            self.resolve_function_header(node)
            return None
        #statements
        elif isinstance(node,BlockNode):
            for v in node.variables():
                v.accept(self)
            self.visit_stmts(node.stmts())
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
            self.bind_type(node.type_node())
            super().visit(node)
            return None
        elif isinstance(node,SizeofExprNode):
            self.bind_type(node.type_node())
            super().visit(node)
            return None
        elif isinstance(node,SizeofTypeNode):
            self.bind_type(node.operand_type_node())
            self.bind_type(node.type_node())
            super().visit(node)
            return None
        elif isinstance(node,VariableNode):
            return None
        elif isinstance(node,IntegerLiteralNode):
            self.bind_type(node.type_node())
            return None
        elif isinstance(node,StringLiteralNode):
            self.bind_type(node.type_node())
            return None

        return None