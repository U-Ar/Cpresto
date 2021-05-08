from .Stmt import Stmt

class Switch(Stmt):
    def __init__(self,loc,cond,cases,default,end):
        super().__init__(loc)
        self._cond = cond
        self._cases = cases
        self._default_label = default
        self._end_label = end
    
    def cond(self):
        return self._cond
    def cases(self):
        return self._cases
    def default_label(self):
        return self._default_label
    def end_label(self):
        return self._end_label

    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("cond",self._cond)
        dumper.print_members("cases",self._cases)
        dumper.print_member("default_label",self._default_label)
        dumper.print_member("end_label",self._end_label)
