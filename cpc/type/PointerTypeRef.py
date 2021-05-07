from .TypeRef import TypeRef

class PointerTypeRef(TypeRef):
    def __init__(self,base_type):
        super().__init__(base_type.location)
        self.base_type = base_type
    
    def is_pointer(self):
        return True
    
    def base_type(self):
        return self.base_type
    
    def equals(self,other):
        if not isinstance(other,PointerTypeRef):
            return False
        return self.base_type.equals(other.base_type())
    
    def to_string(self):
        return self.base_type.to_string() + "*"