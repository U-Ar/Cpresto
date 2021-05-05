from .UnaryOpNode import UnaryOpNode

class UnaryArithmeticOpNode(UnaryOpNode):
    def __init__(self, op, expr):
        super().__init__(op,expr)
        self.amount = 1
    
    def set_expr(self,expr):
        self.expr = expr
    
    def amount(self):
        return self.amount
    
    def set_amount(self,amount):
        self.amount = amount
    