from .Type import Type

class PointerType(Type):
    def __init__(self,size,base_type):
        self.size = size
        self.base_type = base_type

    def is_pointer(self):
        return True
    def is_scalar(self):
        return True
    def is_signed(self):
        return False
    def is_callable(self):
        return self.base_type.is_function()
    
    def size(self):
        return self.size

    def base_type(self):
        return self.base_type
    
    def equals(self,other):
        if not isinstance(other,PointerType):
            return False
        return self.base_type.equals(other.get_pointer_type().base_type())
    
    def is_same_type(self,other):
        if not other.is_pointer():
            return False
        return self.base_type.is_same_type(other.base_type())
    
    def is_compatible(self,other):
        if not other.is_pointer():
            return False
        if self.base_type.is_void():
            return True
        if other.base_type.is_void():
            return True
        return self.base_type.is_compatible(other.base_type)
    
    def is_castable_to(self,other):
        return other.is_pointer() or other.is_integer()
    
    def to_string(self):
        return self.base_type.to_string() + "*"
