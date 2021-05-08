from .Stmt import Stmt

class ExprStmt(Stmt):
    def __init__(self,loc,expr):
        self.__init__(loc)
        self._expr = expr
    
    def expr(self):
        return self._expr
    
    def accpet(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("expr",self._expr)