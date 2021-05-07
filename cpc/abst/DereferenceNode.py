from .LHSNode import LHSNode

class DereferenceNode(LHSNode):
    def __init__(self,expr):
        self._expr = expr
    
    def orig_type(self):
        return self._expr.type().base_type()
    
    def expr(self):
        return self._expr
    
    def set_expr(self,expr):
        self._expr = expr
    
    def location(self):
        return self._expr.location()
    
    def _dump(self,dumper):
        if self.type != None:
            dumper.print_member("type",self.type())
        dumper.print_member("expr",self._expr)
    
    def accept(self,visitor):
        return visitor.visit(self)