from .UnaryOpNode import UnaryOpNode

class UnaryArithmeticOpNode(UnaryOpNode):
    def __init__(self, op, expr):
        super().__init__(op,expr)
        self._amount = 1
    
    def set_expr(self,expr):
        self._expr = expr
    
    def amount(self):
        return self._amount
    
    def set_amount(self,amount):
        self._amount = amount
    