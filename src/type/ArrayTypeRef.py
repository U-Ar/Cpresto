from .TypeRef import TypeRef

class ArrayTypeRef(TypeRef):
    undefined = -1

    def __init__(self,base_type,length=None):
        super().__init__(base_type.location())
        if length == None:
            self.length = ArrayTypeRef.undefined
        elif length < 0:
            raise Exception("negative array length")
        else:
            self.length = length
        self.base_type = base_type
    
    def is_array(self):
        return True
    
    def equals(self,other):
        return isinstance(other,ArrayTypeRef) and (self.length == other.length())
    
    def base_type(self):
        return self.base_type
    
    def length(self):
        return self.length
    
    def is_length_undefined(self):
        return self.length == ArrayTypeRef.undefined
    
    def to_string(self):
        if self.length == ArrayTypeRef.undefined:
            return self.base_type.to_string() + "[]"
        else:
            return self.base_type.to_string() + "[" + str(self.length) + "]"
    
