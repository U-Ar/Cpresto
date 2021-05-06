from .ExprNode import ExprNode

class AddressNode(ExprNode):
    def __init__(self,expr):
        self.expr = expr
        self.type = None
    
    def expr(self):
        return self.expr
    
    def type(self):
        if self.type == None:
            raise Exception("type is null")
        return self.type
    
    def set_type(self,t):
        if self.type != None:
            raise Exception("type set twice")
        self.type = t
    
    def location(self):
        return self.expr.location()
    
    def _dump(self,dumper):
        if self.type == None:
            dumper.print_member("type", self.type)
        dumper.print_member("expr", self.expr)

    def accept(self,visitor):
        return visitor.visit(self)