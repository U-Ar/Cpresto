from .ExprNode import ExprNode
from .TypeNode import TypeNode

class SizeofExprNode(ExprNode):
    def __init__(self, expr, t):
        self.expr = expr
        self.type = TypeNode(t)
    
    def expr(self):
        return self.expr
    
    def set_expr(self,expr):
        self.expr = expr
    
    def type(self):
        return self.type.type()
    
    def type_node(self):
        return self.type
    
    def location(self):
        return self.expr.location()
    
    def _dump(self,dumper):
        dumper.print_member("expr",self.expr)
    
    def accept(self,visitor):
        return visitor.visit(self)