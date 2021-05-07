from .ExprNode import ExprNode

class UnaryOpNode(ExprNode):
    def __init__(self,op,expr):
        self._operator = op
        self._expr = expr
    
    def operator(self):
        return self._operator
    
    def type(self):
        return self._expr.type()
    
    def set_op_type(self,t):
        self.op_type = t
    
    def op_type(self):
        return self.op_type
    
    def expr(self):
        return self._expr
    
    def set_expr(self,expr):
        self._expr = expr
    
    def location(self):
        return self._expr.location()
    
    def _dump(self,dumper):
        dumper.print_member("operator",self._operator)
        dumper.print_member("expr",self._expr)
    
    def accept(self,visitor):
        return visitor.visit(self)