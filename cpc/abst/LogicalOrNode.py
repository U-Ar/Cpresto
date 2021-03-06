from .BinaryOpNode import BinaryOpNode

class LogicalOrNode(BinaryOpNode):
    def __init__(self,left,right):
        super().__init__(left,"||",right)
    
    def accept(self,visitor):
        return visitor.visit(self)