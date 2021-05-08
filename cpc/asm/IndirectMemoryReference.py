from .MemoryReference import MemoryReference
from .SymbolTable import SymbolTable
from .IntegerLiteral import IntegerLiteral

class IndirectMemoryReference(MemoryReference):
    def __init__(self,offset,base,fixed=True):
        if isinstance(offset,int):
            self._offset = IntegerLiteral(offset)
        else :
            self._offset = offset
        self._base = base
        self._fixed = fixed

    @staticmethod
    def relocatable(offset,base):
        return IndirectMemoryReference(IntegerLiteral(offset),self._base,False)
    
    def offset(self):
        return self._offset

    def fix_offset(self,dif):
        if self._fixed:
            raise Exception("must not happen: fixed = True")
        curr = self._offset.value()
        self._offset = IntegerLiteral(curr + dif)
        self._fixed = True

    def base(self):
        return self._base

    def collect_statistics(self,stats):
        self._base.collect_statistics(stats)

    def to_string(self):
        return self.to_source(SymbolTable.dummy())
    
    def to_source(self,table):
        if not self._fixed:
            raise Exception("must not happen: writing unfixed variable")
        return "" if self._offset.is_zero() else \
            self._offset.to_source(table) + "(" + self._base.to_source(table) + ")"
    
    def compare_to(self,mem):
        return -(mem.cmp(self))
    
    def cmp(self,mem):
        if isinstance(mem,IndirectMemoryReference):
            return self._offset.compare_to(mem._offset)
        else :
            return -1
    
    def dump(self):
        return "(IndirectMemoryReference "\
            + ("" if self._fixed else "*") \
                + self._offset.dump() + " " + self._base.dump()+")"
    
