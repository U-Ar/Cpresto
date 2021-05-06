from .StmtNode import StmtNode

class ExprStmtNode(StmtNode):
    def __init__(self,loc,expr):
        super().__init__(loc)
        self.expr = expr
    
    def expr(self):
        return self.expr
    
    def set_expr(self,expr):
        self.expr = expr
    
    def _dump(self,dumper):
        dumper.print_member("expr", expr)
    
    def accept(self,visitor):
        return visitor.visit(self)