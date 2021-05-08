from .Expr import Expr

class Mem(Expr):
    def __init__(self,t,expr):
        super().__init__(t)
        self._expr = expr

    def expr(self):
        return self._expr

    def address_node(self,t):
        return self._expr
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("expr",self._expr)