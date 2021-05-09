from utils.TextUtils import TextUtils
from .Symbol import Symbol

class SuffixedSymbol(Symbol):
    def __init__(self,base,suffix):
        self._base = base
        self._suffix = suffix
    
    def is_zero(self):
        return False

    def collect_statistics(self,stats):
        self._base.collect_statistics(stats)

    def plus(self,n):
        raise Exception("must not happen: SuffixedSymbol.plus called")
    
    def name(self):
        return self._base.name()
    
    def to_source(self,table=None):
        if table == None:
            return self._base.to_source() + self._suffix
        else :
            return self._base.to_source(table) + self._suffix

    def to_string(self):
        return self._base.to_string() + self._suffix
    
    def compare_to(self,lit):
        return -(lit.compare_to(self))
    
    def cmp(self,i):
        if isinstance(i,IntegerLiteral):
            return 1
        elif isinstance(i,NamedSymbol) or isinstance(i,SuffixedSymbol):
            s1 = self.to_string()
            s2 = i.to_string()
            if s1 > s2:
                return 1
            elif s1 < s2:
                return -1
            else :
                return 0
        else:
            return -1
    
    def dump(self):
        return "(SuffixedSymbol " + self._base.dump() + \
            " " + TextUtils.dump_string(self._suffix) + ")"