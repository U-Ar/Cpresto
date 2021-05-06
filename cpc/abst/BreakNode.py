class BreakNode(StmtNode):
    def __init__(self,loc):
        super().__init__(loc)
    
    def _dump(self,dumper):
        pass

    def accept(self,visitor):
        return visitor.visit(self)