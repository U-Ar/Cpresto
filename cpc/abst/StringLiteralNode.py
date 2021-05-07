from .LiteralNode import LiteralNode

class StringLiteralNode(LiteralNode):
    def __init__(self,loc,ref,value):
        super().__init__(loc,ref)
        self._value = value
        self._entry = None
    
    def value(self):
        return self._value

    def entry(self):
        return self._entry

    def set_entry(self,ent):
        self._entry = ent
    
    def _dump(self,dumper):
        dumper.print_member("value",self._value)
    
    def accept(self,visitor):
        return visitor.visit(self)
    