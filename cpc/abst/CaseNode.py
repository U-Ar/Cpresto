from asm.Label import Label
from .StmtNode import StmtNode

class CaseNode(StmtNode):
    def __init__(self,loc,values,body):
        super().__init__(loc)
        self._values = values
        self._body = body
        self._label = Label()

    def values(self):
        return self._values
    
    def is_default(self):
        return len(self._values) == 0
    
    def body(self):
        return self._body
    
    def label(self):
        return self._label
    
    def _dump(self,dumper):
        dumper.print_node_list("values",values)
        dumper.print_member("body", body)
    
    def accept(self,visitor):
        return visitor.visit(self)