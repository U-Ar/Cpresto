from .ExprNode import ExprNode
from .TypeNode import TypeNode

class SizeofExprNode(ExprNode):
    def __init__(self, expr, t):
        self._expr = expr
        self._type = TypeNode(t)
    
    def expr(self):
        return self._expr
    
    def set_expr(self,expr):
        self._expr = expr
    
    def type(self):
        return self._type.type()
    
    def type_node(self):
        return self._type
    
    def location(self):
        return self._expr.location()
    
    def _dump(self,dumper):
        dumper.print_member("expr",self._expr)
    
    def accept(self,visitor):
        return visitor.visit(self)