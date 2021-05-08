from .Expr import Expr

class Uni(Expr):
    def __init__(self,t,op,expr):
        super().__init__(t)
        self._op = op
        self._expr = expr
    
    def op(self):
        return self._op
    def expr(self):
        return self._expr
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("op",self._op.to_string())
        dumper.print_member("expr",self._expr)