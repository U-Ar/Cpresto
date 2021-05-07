from .StmtNode import StmtNode

class LabelNode(StmtNode):
    def __init__(self,loc,name,stmt):
        super().__init__(loc)
        self._name = name
        self._stmt = stmt
    
    def name(self):
        return self._name
    
    def stmt(self):
        return self._stmt
    
    def _dump(self,dumper):
        dumper.print_member("name",self._name)
        dumper.print_member("stmt",self._stmt)
    
    def accept(self,visitor):
        return visitor.visit(self)