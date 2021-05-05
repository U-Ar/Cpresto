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
#added:   StructNode, UnionNode, TypedefNode, 
#         DefinedVariable, UndefinedVariable, Constant,
#         DefinedFunction, Undefinedfunction
from ..entity.DefinedVariable import DefinedVariable
from ..entity.UndefinedVariable import UndefinedVariable
from ..entity.Constant import Constant
from ..entity.DefinedFunction import DefinedFunction
from ..entity.Undefinedfunction import Undefinedfunction

from ..exception.SemanticException import SemanticException
from Visitor import Visitor

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