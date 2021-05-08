from .Operand import Operand
from .IntegerLiteral import IntegerLiteral

class ImmediateValue(Operand):
    def __init__(self,n):
        if isinstance(n,int):
            self._expr = IntegerLiteral(n)
        else :
            self._expr = n

    def equals(self,other):
        if not isinstance(other,ImmediateValue):
            return False
        return self._expr.equals(other.expr())
    
    def expr(self):
        return self._expr

    def collect_statistics(self,stats):
        pass

    def to_source(self,table):
        return "$" + self._expr.to_source(table)
    
    def dump(self):
        return "(ImmediateValue " + self._expr.dump() + ")"