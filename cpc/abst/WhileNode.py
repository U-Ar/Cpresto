from .StmtNode import StmtNode

class WhileNode(StmtNode):
    def __init__(self,loc,cond,body):
        super().__init__(loc)
        self._cond = cond
        self._body = body
    
    def cond(self):
        return self._cond
    
    def body(self):
        return self._body
    
    def _dump(self,dumper):
        dumper.print_member("cond",self._cond)
        dumper.print_member("body",self._body)
    
    def accept(self,visitor):
        return visitor.visit(self)
