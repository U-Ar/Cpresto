from .ExprStmtNode import ExprStmtNode
from .StmtNode import StmtNode

class ForNode(StmtNode):
    def __init__(self,loc,init,cond,incr,body):
        super().__init__(loc)
        self._init = ExprStmtNode(init.location(),init)
        self._cond = cond
        self._incr = ExprStmtNode(incr.location(),incr)
        self._body = body

    def init(self):
        return self._init
    
    def cond(self):
        return self._cond
    
    def incr(self):
        return self._incr
    
    def body(self):
        return self._body
    
    def _dump(self,dumper):
        dumper.print_member("init",self._init)
        dumper.print_member("cond",self._cond)
        dumper.print_member("incr",self._incr)
        dumper.print_member("body",self._body)
    
    def accept(self,visitor):
        return visitor.visit(self)