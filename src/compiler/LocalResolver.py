from .Visitor import Visitor
from ..entity.ConstantTable import ConstantTable
from ..entity.ToplevelScope import ToplevelScope
from ..entity.LocalScope import LocalScope
from ..ast.AST import AST
from ..ast.Node import Node
from ..ast.Location import Location
from ..ast.ExprNode import ExprNode
from ..ast.StmtNode import StmtNode
from ..ast.BlockNode import BlockNode
from ..ast.VariableNode import VariableNode
from ..ast.StringLiteralNode import StringLiteralNode
from ..exception.SemanticException import SemanticException

class LocalResolver(Visitor):
    def __init__(self,h):
        self.error_handler = h
        self.scope_stack = []
        self.constant_table = ConstantTable()
    
    def resolve(self,n):
        if isinstance(n,AST):
            toplevel = ToplevelScope()
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
    
    def visit(self,node):
        if isinstance(node,BlockNode):
            self.push_scope(node.variables())
            super().visit(node)
            node.set_scope(self.pop_scope())
            return None
        elif isinstance(node,StringLiteralNode):
            node.set_entry(self.constant_table.intern(node.value()))
            return None
        elif isinstance(node,VariableNode):
            try:
                ent = self.current_scope().get(node.name())
                ent.refered()
                node.set_entity(ent)
            except SemanticException as ex:
                self.error(node, ex.message)
            return None
    
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
            self.error_handler.error(node,message)
        else:
            self.error_handler.error(node.location(),message)