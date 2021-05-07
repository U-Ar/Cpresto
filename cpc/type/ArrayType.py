from .Type import Type

class ArrayType(Type):
    undefined = -1

    def __init__(self,base_type,pointer_size,length=None):
        self.base_type = base_type
        self.pointer_size = pointer_size
        if length == None:
            self.length = ArrayType.undefined
        else:
            self.length = length
    
    def is_array(self):
        return True
    
    def is_allocated_array(self):
        return (self.length != ArrayType.undefined) and \
                ((not self.base_type.is_array()) or self.base_type.is_allocated_array())
    
    def is_incomplete_array(self):
        if not self.base_type.is_array():
            return False
        return not self.base_type.is_allocated_array()

    def base_type(self):
        return self.base_type

    def length(self):
        return self.length

    def size(self):
        return self.pointer_size
    
    def alloc_size(self):
        if self.length == ArrayType.undefined:
            return self.size()
        else :
            return self.base_type.alloc_size() * self.length
        
    def alignment(self):
        return self.base_type.alignment()
    
    def equals(self,other):
        if not isinstance(other,ArrayType):
            return False
        return self.base_type.equals(other.base_type) and self.length == other.length
    
    def is_same_type(self,other):
        if (not other.is_pointer()) and (not other.is_array()):
            return False
        return self.base_type.is_same_type(other.base_type())
    
    def is_compatible(self,target):
        if (not target.is_pointer()) and (not target.is_array()):
            return False
        if target.base_type().is_void():
            return True
        return self.base_type.is_compatible(target.base_type()) and (self.base_type.size() == target.base_type().size())

    def is_castable_to(self,target):
        return target.is_pointer() or target.is_array()
    
    def to_string(self):
        if self.length < 0:
            return self.base_type.to_string() + "[]"
        else :
            return self.base_type.to_string() + "[" + self.length + "]"
    