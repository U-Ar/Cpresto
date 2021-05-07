from .StmtNode import StmtNode

class SwitchNode(StmtNode):
    def __init__(self,loc,cond,cases):
        super().__init__(loc)
        self._cond = cond
        self._cases = cases
    
    def cond(self):
        return self._cond
    
    def cases(self):
        return self._cases
    
    def _dump(self,dumper):
        dumper.print_member("cond",self._cond)
        dumper.print_node_list("cases",self._cases)
    
    def accept(self,visitor):
        return visitor.visit(self)