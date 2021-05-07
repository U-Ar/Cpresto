from .StmtNode import StmtNode

class IfNode(StmtNode):
    def __init__(self,loc,c,t,e):
        super().__init__(loc)
        self._cond = c
        self._then_body = t
        self._else_body = e
    
    def cond(self):
        return self._cond
    
    def then_body(self):
        return self._then_body
    
    def else_body(self):
        return self._else_body
    
    def _dump(self,dumper):
        dumper.print_member("cond",self._cond)
        dumper.print_member("then_body",self._then_body)
        dumper.print_member("else_body",self._else_body)
    
    def accept(self,visitor):
        return visitor.visit(self)