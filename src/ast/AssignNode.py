class AssignNode(AbstractAssignNode):
    def __init__(self,lhs,rhs):
        super().__init__(lhs,rhs)
    
    def accept(self,visitor):
        return visitor.visit(self)