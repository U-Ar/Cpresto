from .Operand import Operand

class AbsoluteAddress(Operand):
    def __init__(self,reg):
        self._register = reg

    def register(self):
        return self._register

    def collect_statistics(self,stats):
        self._register.collect_statistics(stats)
    
    def to_source(self,table):
        return "*" + self._register.to_source(table)
    
    def dump(self):
        return "(AbsoluteAddress " + self._register.dump() + ")"
