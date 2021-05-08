from .StmtNode import StmtNode

class DoWhileNode(StmtNode):
    def __init__(self,loc,body,cond):
        super().__init__(loc)
        self._body = body
        self._cond = cond
    
    def body(self):
        return self._body
    
    def cond(self):
        return self._cond
    
    def _dump(self,dumper):
        dumper.print_member("body",self._body)
        dumper.print_member("cond",self._cond)
    
    def accept(self,visitor):
        return visitor.visit(self)