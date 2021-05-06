from .ExprNode import ExprNode

class UnaryOpNode(ExprNode):
    def __init__(self,op,expr):
        self.operator = op
        self.expr = expr
    
    def operator(self):
        return self.operator
    
    def type(self):
        return self.expr.type()
    
    def set_op_type(self,t):
        self.op_type = t
    
    def op_type(self):
        return self.op_type
    
    def expr(self):
        return self.expr
    
    def set_expr(self,expr):
        self.expr = expr
    
    def location(self):
        return self.expr.location()
    
    def _dump(self,dumper):
        dumper.print_member("operator",self.operator)
        dumper.print_member("expr",self.expr)
    
    def accept(self,visitor):
        return visitor.visit(self)