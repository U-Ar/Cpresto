from Type import Type

class VoidType(Type):
    def __init__(self):
        pass

    def is_void(self):
        return True
    
    def size(self):
        return 1
    
    def equals(self,other):
        return isinstance(other,VoidType)
    
    def is_same_type(self, other):
        return other.is_void()
    
    def is_compatible(self,other):
        return other.is_void()
    
    def is_castable_to(self,other):
        return other.is_void()
    
    def to_string(self):
        return "void"