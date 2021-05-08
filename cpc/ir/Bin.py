from .Expr import Expr

class Bin(Expr):
    def __init__(self,t,op,left,right):
        super().__init__(t)
        self._op = op
        self._left = left
        self._right = right
    
    def left(self):
        return self._left
    def right(self):
        return self._right
    def op(self):
        return self._op
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("op",self._op.to_string())
        dumper.print_member("left",self._left)
        dumper.print_member("right",self._right)