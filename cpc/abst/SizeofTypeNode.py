from .ExprNode import ExprNode
from .TypeNode import TypeNode

class SizeofTypeNode(ExprNode):
    def __init__(self,operand,t):
        self._operand = operand
        self._type = TypeNode(t)
    
    def operand(self):
        return self._operand.type()
    
    def operand_type_node(self):
        return self._operand
    
    def type(self):
        return self._type.type()
    
    def type_node(self):
        return self._type

    def location(self):
        return self._operand.location()
    
    def _dump(self,dumper):
        dumper.print_member("operand",self._type)
    
    def accept(self,visitor):
        return visitor.visit(self)