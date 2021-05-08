from .Literal import Literal

class IntegerLiteral(Literal):
    def __init__(self,n):
        self._value = n

    def equals(self,other):
        return isinstance(other,IntegerLiteral) and (self._value == other._value)
    
    def value(self):
        return self._value
    
    def is_zero(self):
        return self._value == 0
    
    def plus(self,dif):
        return IntegerLiteral(self._value + dif)
    
    def integer_literal(self):
        return self

    def to_source(self):
        return str(self._value)
    
    def collect_statistics(self):
        pass

    def to_string(self):
        return str(self._value)
    
    def compare_to(self,lit):
        return -(lit.cmp(self))
    
    def cmp(self,sym):
        if isinstance(sym,IntegerLiteral):
            if self._value > sym._value:
                return 1
            elif self._value < sym._value:
                return -1
            else :
                return 0
        else :
            return -1


    def dump(self):
        return "(IntegerLiteral " + str(self._value) + ")"