from .StmtNode import StmtNode

class GotoNode(StmtNode):
    def __init__(self,loc,target):
        super().__init__(loc)
        self._target = target
    
    def target(self):
        return self._target
    
    def _dump(self,dumper):
        dumper.print_member("target",self._target)
    
    def accept(self,visitor):
        return visitor.visit(self)