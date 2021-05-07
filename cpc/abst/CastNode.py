from type.Type import Type
from .TypeNode import TypeNode
from .ExprNode import ExprNode

class CastNode(ExprNode):
    def __init__(self,t,expr):
        if isinstance(t,TypeNode):
            self._type_node = t
        else :
            self._type_node = TypeNode(t)
        self._expr = expr
    
    def type(self):
        return self._type_node.type()
    
    def type_node(self):
        return self._type_node
    
    def expr(self):
        return self._expr
    
    def is_lvalue(self):
        return self._expr.is_lvalue()
    
    def is_assignable(self):
        return self._expr.is_assignable()
    
    def is_effective_cast(self):
        return self.type().size() > self._expr.type().size()

    def location(self):
        return self._type_node.location()

    def _dump(self,dumper):
        dumper.print_member("TypeNode", self._type_node)
        dumper.print_member("expr", self._expr)
    
    def accept(self,visitor):
        return visitor.visit(self)
