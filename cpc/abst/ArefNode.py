from .LHSNode import LHSNode

class ArefNode(LHSNode):
    def __init__(self,expr,index):
        self.expr = expr
        self.index = index
    
    def expr(self):
        return self.expr
    
    def index(self):
        return self.index
    
    def is_multi_dimension(self):
        return isinstance(self.expr,ArefNode) and not self.expr.orig_type().is_pointer()

    def base_expr(self):
        return self.expr.base_expr() if self.is_multi_dimension() else self.expr
    
    def element_size(self):
        return self.orig_type().alloc_size()
    
    def length(self):
        return self.expr.orig_type().length()
    
    def orig_type(self):
        return self.expr.orig_type().base_type()
    
    def location(self):
        return self.expr.location()

    def _dump(self,dumper):
        if self.type == None:
            dumper.print_member("type",self.type)
        dumper.print_member("expr", expr)
        dumper.print_member("index", index)
    
    def accept(self,visitor):
        return visitor.visit(self)
