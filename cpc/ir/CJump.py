from .Stmt import Stmt

class CJump(Stmt):
    def __init__(self,loc,cond,then_label,else_label):
        super().__init__(loc)
        self._cond = cond
        self._then_label = then_label
        self._else_label = else_label
    
    def cond(self):
        return self._cond
    def then_label(self):
        return self._then_label
    def else_label(self):
        return self._else_label
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("cond",self._cond)
        dumper.print_member("then_label",self._then_label)
        dumper.print_member("else_label",self._else_label)