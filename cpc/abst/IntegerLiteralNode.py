from .LiteralNode import LiteralNode

class IntegerLiteralNode(LiteralNode):
    def __init__(self,loc,ref,value):
        super().__init__(loc,ref)
        self._value = value
    
    def value(self):
        return self._value
    
    def _dump(self,dumper):
        dumper.print_member("type_node", self.type_node())
        dumper.print_member("value", self._value)
    
    def accept(self,visitor):
        return visitor.visit(self)