from .UnaryArithmeticOpNode import UnaryArithmeticOpNode

class SuffixOpNode(UnaryArithmeticOpNode):
    def __init__(self,op,expr):
        super().__init__(op,expr)

    def accept(self,visitor):
        return visitor.visit(self)