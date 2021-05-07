from .ExprNode import ExprNode

class AddressNode(ExprNode):
    def __init__(self,expr):
        self._expr = expr
        self._type = None
    
    def expr(self):
        return self._expr
    
    def type(self):
        if self._type == None:
            raise Exception("type is null")
        return self._type
    
    def set_type(self,t):
        if self._type != None:
            raise Exception("type set twice")
        self._type = t
    
    def location(self):
        return self._expr.location()
    
    def _dump(self,dumper):
        if self._type == None:
            dumper.print_member("type", self._type)
        dumper.print_member("expr", self._expr)

    def accept(self,visitor):
        return visitor.visit(self)