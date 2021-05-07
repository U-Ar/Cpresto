from .TypeNode import TypeNode
from .ExprNode import ExprNode

class LiteralNode(ExprNode):
    def __init__(self,loc,ref):
        super().__init__()
        self._location = loc
        self._type_node = TypeNode(ref)
    
    def location(self):
        return self._location
    
    def type(self):
        return self._type_node.type()
    
    def type_node(self):
        return self._type_node
    
    def is_constant(self):
        return True