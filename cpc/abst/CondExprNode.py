class CondExprNode(ExprNode):
    def __init__(self,cond,t,e):
        super().__init__()
        self.cond = cond
        self.then_expr = t
        self.else_expr = e
    
    def type(self):
        return self.then_expr.type()
    
    def cond(self):
        return self.cond
    
    def then_expr(self):
        return self.then_expr
    
    def set_then_expr(self,expr):
        self.then_expr = expr
    
    def else_expr(self):
        return self.else_expr
    
    def set_else_expr(self,expr):
        self.else_expr = expr
    
    def location(self):
        return self.cond.location()
    
    def _dump(self, dumper):
        dumper.print_member("cond",self.cond)
        dumper.print_member("then_expr",self.then_expr)
        dumper.print_member("else_expr",self.else_expr)
    
    def accept(self,visitor):
        return visitor.visit(self)