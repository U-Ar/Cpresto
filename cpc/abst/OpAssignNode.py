from .AbstractAssignNode import AbstractAssignNode

class OpAssignNode(AbstractAssignNode):
    def __init__(self,lhs,op,rhs):
        super().__init__(lhs,rhs)
        self.operator = op
    
    def operator(self):
        return self.operator
    
    def accept(self,visitor):
        return visitor.visit(self)