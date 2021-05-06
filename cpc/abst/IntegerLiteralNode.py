class IntegerLiteralNode(LiteralNode):
    def __init__(self,loc,ref,value):
        super().__init__(loc,ref)
        self.value = value
    
    def value(self):
        return self.value
    
    def _dump(self,dumper):
        dumper.print_member("type_node", self.type_node)
        dumper.print_member("value", self.value)
    
    def accept(self,visitor):
        return visitor.visit(self)