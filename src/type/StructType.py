from .CompositeType import CompositeType
from ..utils.AsmUtils import AsmUtils

class StructType(CompositeType):
    def __init__(self,name,membs,loc):
        super().__init__(name,membs,loc)
    
    def is_struct(self):
        return True
    
    def is_same_type(self,other):
        if not other.is_struct():
            return False
        #?same instance
        return self is other.get_struct_type()
    
    def compute_offsets(self):
        offset = 0
        max_align = 1
        for s in self.members:
            offset = AsmUtils.align(offset, s.alloc_size())
            s.set_offset(offset)
            offset += s.alloc_size()
            max_align = max(max_align,s.alignment())
        self.cached_size = AsmUtils.align(offset, max_align)
        self.cached_align = max_align
    
    def to_string(self):
        return "struct " + self.name
    
