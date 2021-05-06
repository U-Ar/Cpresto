from TypeRef import TypeRef

class VoidTypeRef(TypeRef):
    def __init__(self,loc=None):
        super().__init__(loc)
    
    def is_void(self):
        return True
    
    def equals(self,other):
        return isinstance(other,VoidTypeRef)
    
    def to_string(self):
        return "void"