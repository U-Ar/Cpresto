from CompositeType import CompositeType
from ..utils.AsmUtils import AsmUtils

class UnionType(CompositeType):
    def __init__(self,name,membs,loc):
        super().__init__(name,membs,loc)
    
    def is_union(self):
        return True
    
    def is_same_type(self,other):
        if not other.is_union():
            return False
        return self is other.get_union_type()
    
    def compute_offsets(self):
        max_size = 0
        max_align = 1
        for s in self.members:
            s.set_offset(0)
            max_size = max(max_size,s.alloc_size())
            max_align = max(max_align,s.alignment())
        self.cached_size = AsmUtils.align(max_size,max_align)
        self.cached_align = max_align
    
    def to_string(self):
        return "union " + self.name