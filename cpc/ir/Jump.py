from .Stmt import Stmt

class Jump(Stmt):
    def __init__(self,loc,label):
        super().__init__(loc)
        self._label = label

    def label(self):
        return self._label
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("label",self._label)