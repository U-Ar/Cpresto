from NamedType import NamedType

class UserType(NamedType):
    def __init__(self,name,real,loc):
        super().__init__(name,loc)
        self.real = real
    
    def real_type(self):
        return self.real.type()
    
    def to_string(self):
        return self.name
    
    def size(self):
        return self.real_type().size()
    def alloc_size(self):
        return self.real_type().alloc_size()
    def alignment(self):
        return self.real_type().alignment()
    
    def is_void(self):
        return self.real_type().is_void()
    def is_int(self):
        return self.real_type().is_int()
    def is_integer(self):
        return self.real_type().is_integer()
    def is_signed(self):
        return self.real_type().is_signed()
    def is_pointer(self):
        return self.real_type().is_pointer()
    def is_array(self):
        return self.real_type().is_array()
    def is_allocated_array(self):
        return self.real_type().is_allocated_array()
    def is_composite_type(self):
        return self.real_type().is_composite_type()
    def is_struct(self):
        return self.real_type().is_struct()
    def is_union(self):
        return self.real_type().is_union()
    def is_user_type(self):
        return True
    def is_function(self):
        return self.real_type().is_function()
    
    def is_callable(self):
        return self.real_type().is_callable()
    def is_scalar(self):
        return self.real_type().is_scalar()
    
    def base_type(self):
        return self.real_type().base_type()
    
    def is_same_type(self,other):
        return self.real_type().is_same_type(other)
    def is_compatible(self,other):
        return self.real_type().is_compatible(other)
    def is_castable_to(self,other):
        return self.real_type().is_castable_to(other)
    
    def get_integer_type(self):
        return self.real_type().get_integer_type()
    def get_composite_type(self):
        return self.real_type().get_composite_type()
    def get_struct_type(self):
        return self.real_type().get_struct_type()
    def get_union_type(self):
        return self.real_type().get_union_type()
    def get_array_type(self):
        return self.real_type().get_array_type()
    def get_pointer_type(self):
        return self.real_type().get_pointer_type()
    def get_function_type(self):
        return self.real_type().get_function_type()
    
