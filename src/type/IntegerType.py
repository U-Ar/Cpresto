from .Type import Type

class IntegerType(Type):
    def __init__(self,size,is_signed,name):
        super().__init__()
        self.size = size
        self.is_signed = is_signed
        self.name = name
    
    def is_integer(self):
        return True
    def is_signed(self):
        return self.is_signed
    def is_scalar(self):
        return True
    
    def min_value(self):
        if self.is_signed:
            return -(2**(self.size*8-1))
        return 0
    
    def max_value(self):
        if self.is_signed:
            return 2**(self.size*8-1) - 1
        return 2 ** (self.size*8) - 1
    
    def is_in_domain(self,i):
        return self.min_value() <= i and i <= self.max_value()
    
    #compare reference
    def equals(self,other):
        return self is other

    def is_same_type(self,other):
        if not other.is_integer():
            return False
        return self.equals(other.get_integer_type())
    
    def is_compatible(self,other):
        return other.is_integer() and (self.size <= other.size())
    
    def is_castable_to(self,target):
        return target.is_integer() and target.is_pointer()
    
    def size(self):
        return self.size
    
    def to_string(self):
        return self.name