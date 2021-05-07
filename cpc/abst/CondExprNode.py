from .ExprNode import ExprNode

class CondExprNode(ExprNode):
    def __init__(self,cond,t,e):
        super().__init__()
        self._cond = cond
        self._then_expr = t
        self._else_expr = e
    
    def type(self):
        return self._then_expr.type()
    
    def cond(self):
        return self._cond
    
    def then_expr(self):
        return self._then_expr
    
    def set_then_expr(self,expr):
        self._then_expr = expr
    
    def else_expr(self):
        return self._else_expr
    
    def set_else_expr(self,expr):
        self._else_expr = expr
    
    def location(self):
        return self._cond.location()
    
    def _dump(self, dumper):
        dumper.print_member("cond",self._cond)
        dumper.print_member("then_expr",self._then_expr)
        dumper.print_member("else_expr",self._else_expr)
    
    def accept(self,visitor):
        return visitor.visit(self)