from .StmtNode import StmtNode

class GotoNode(StmtNode):
    def __init__(self,loc,target):
        super().__init__(loc)
        self.target = target
    
    def target(self):
        return self.target
    
    def _dump(self,dumper):
        dumper.print_member("target",target)
    
    def accept(self,visitor):
        return visitor.visit(self)