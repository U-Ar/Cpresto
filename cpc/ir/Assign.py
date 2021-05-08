from .Stmt import Stmt

class Assign(Stmt):
    def __init__(self,loc,lhs,rhs):
        super().__init__(loc)
        self._lhs = lhs
        self._rhs = rhs

    def lhs(self):
        return self._lhs
    def rhs(self):
        return self._rhs
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("lhs",self._lhs)
        dumper.print_member("rhs",self._rhs)