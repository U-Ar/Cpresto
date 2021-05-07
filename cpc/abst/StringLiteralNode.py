from .LiteralNode import LiteralNode

class StringLiteralNode(LiteralNode):
    def __init__(self,loc,ref,value):
        super().__init__(loc,ref)
        self.value = value
        self.entry = None
    
    def value(self):
        return self.value

    def entry(self):
        return self.entry

    def set_entry(self,ent):
        self.entry = ent
    
    def _dump(self,dumper):
        dumper.print_member("value",value)
    
    def accept(self,visitor):
        return visitor.visit(self)
    