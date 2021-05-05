from ..asm.Label import Label

class CaseNode(StmtNode):
    def __init__(self,loc,values,body):
        super().__init__(loc)
        self.values = values
        self.body = body
        self.label = Label()

    def values(self):
        return self.values
    
    def is_default(self):
        return len(self.values) == 0
    
    def body(self):
        return self.body
    
    def label(self):
        return self.label
    
    def _dump(self,dumper):
        dumper.print_node_list("values",values)
        dumper.print_member("body", body)
    
    def accept(self,visitor):
        return visitor.visit(self)