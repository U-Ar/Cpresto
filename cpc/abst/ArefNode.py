from .LHSNode import LHSNode

class ArefNode(LHSNode):
    def __init__(self,expr,index):
        self._expr = expr
        self._index = index
    
    def expr(self):
        return self._expr
    
    def index(self):
        return self._index
    
    def is_multi_dimension(self):
        return isinstance(self._expr,ArefNode) and not self._expr.orig_type().is_pointer()

    def base_expr(self):
        return self._expr.base_expr() if self.is_multi_dimension() else self._expr
    
    def element_size(self):
        return self.orig_type().alloc_size()
    
    def length(self):
        return self._expr.orig_type().length()
    
    def orig_type(self):
        return self._expr.orig_type().base_type()
    
    def location(self):
        return self._expr.location()

    def _dump(self,dumper):
        if self.type == None:
            dumper.print_member("type",self.type())
        dumper.print_member("expr", self.expr())
        dumper.print_member("index", self.index())
    
    def accept(self,visitor):
        return visitor.visit(self)
