from .BaseSymbol import BaseSymbol
from .IntegerLiteral import IntegerLiteral
from .UnnamedSymbol import UnnamedSymbol
from .SuffixedSymbol import SuffixedSymbol
from utils.TextUtils import TextUtils

class NamedSymbol(BaseSymbol):
    def __init__(self,name):
        self._name = name

    def name(self):
        return self._name

    def to_source(self,table=None):
        return self._name

    def to_string(self):
        return "#" + self._name
    
    def compare_to(self,lit):
        return -(lit.compare_to(self))
    
    def cmp(self,i):
        if isinstance(i,IntegerLiteral):
            return 1
        elif isinstance(i,NamedSymbol):
            return self._name.compare_to(i._name)
        elif isinstance(i,UnnamedSymbol):
            return -1
        elif isinstance(i,SuffixedSymbol):
            s1 = self.to_string()
            s2 = i.to_string()
            if s1 > s2:
                return 1
            elif s1 < s2:
                return -1
            else :
                return 0
    
    def dump(self):
        return "(NamedSymbol " + TextUtils.dump_string(self._name) + ")"