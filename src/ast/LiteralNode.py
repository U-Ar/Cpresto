from .TypeNode import TypeNode

class LiteralNode(ExprNode):
    def __init__(self,loc,ref):
        super().__init__()
        self.location = loc
        self.type_node = TypeNode(ref)
    
    def location(self):
        return self.location
    
    def type(self):
        return self.type_node.type()
    
    def type_node(self):
        return self.type_node
    
    def is_constant(self):
        return True