from .TypeNode import TypeNode

class SizeofTypeNode(ExprNode):
    def __init__(self,operand,t):
        self.operand = operand
        self.type = TypeNode(t)
    
    def operand(self):
        return self.operand.type()
    
    def operand_type_node(self):
        return self.operand
    
    def type(self):
        return self.type.type()
    
    def type_node(self):
        return self.type

    def location(self):
        return self.operand.location()
    
    def _dump(self,dumper):
        dumper.print_member("operand",self.type)
    
    def accept(self,visitor):
        return visitor.visit(self)