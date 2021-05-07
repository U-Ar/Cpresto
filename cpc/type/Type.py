from abc import ABCMeta, abstractmethod
from exception.SemanticError import SemanticError

class Type(metaclass=ABCMeta) :
    size_unknown = -1

    @abstractmethod
    def size(self):
        pass

    def alloc_size(self):
        return self.size()
    
    def alignment(self):
        return self.alloc_size()
    
    @abstractmethod
    def is_same_type(self,other):
        pass

    def is_void(self):
        return False
    
    def is_int(self):
        return False
    
    def is_integer(self):
        return False
    
    def is_signed(self):
        raise Exception("is_signed for non-integer type")
    
    def is_pointer(self):
        return False
    
    def is_array(self):
        return False
    
    def is_composite_type(self):
        return False
    
    def is_struct(self):
        return False
    
    def is_union(self):
        return False
    
    def is_user_type(self):
        return False
    
    def is_function(self):
        return False
    
    def is_allocated_array(self):
        return False
    
    def is_incomplete_array(self):
        return False
    
    def is_scalar(self):
        return False
    
    def is_callable(self):
        return False
    
    @abstractmethod
    def is_compatible(self,other):
        pass

    @abstractmethod
    def is_castable_to(self,target):
        pass

    def base_type(self):
        raise SemanticError("base_type called for undereferable type")
    
    def get_integer_type(self):
        return self
    def get_pointer_type(self):
        return self
    def get_function_type(self):
        return self
    def get_struct_type(self):
        return self
    def get_union_type(self):
        return self
    def get_composite_type(self):
        return self
    def get_array_type(self):
        return self

    


