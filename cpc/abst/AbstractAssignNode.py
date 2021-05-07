from .ExprNode import ExprNode

class AbstractAssignNode(ExprNode):
    def __init__(self,lhs,rhs):
        super().__init__()
        self._lhs=lhs
        self._rhs=rhs
    
    def type(self):
        return self._lhs.type()
    
    def lhs(self):
        return self._lhs
    
    def rhs(self):
        return self._rhs
    
    def set_rhs(self,expr):
        self._rhs = expr
    
    def location(self):
        return self._lhs.location()
    
    def _dump(self,dumper):
        dumper.print_member("lhs",self._lhs)
        dumper.print_member("rhs",self._rhs)
