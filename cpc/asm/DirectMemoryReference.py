from .MemoryReference import MemoryReference
from .SymbolTable import SymbolTable

class DirectMemoryReference(MemoryReference):
    def __init__(self,val):
        self._value = val

    def value(self):
        return self._value

    def collect_statistics(self,stats):
        self._value.collect_statistics(stats)

    def fix_offset(self,dif):
        raise Exception("DirectMemoryReference.fix_offset")
    
    def to_string(self):
        return self.to_source(SymbolTable.dummy())

    def to_source(self,table):
        return self._value.to_source(table)
    
    def compare_to(self,mem):
        return -(mem.cmp(self))
    
    def cmp(self,mem):
        if isinstance(mem,DirectMemoryReference):
            return self._value.compare_to(mem.value)
        else:
            return 1
    
    def dump(self):
        return "(DirectMemoryReference " + self._value.dump() + ")"
