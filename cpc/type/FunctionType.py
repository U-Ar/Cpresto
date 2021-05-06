from .Type import Type

class FunctionType(Type):
    def __init__(self,ret,partypes):
        self.return_type = ret
        self.param_types = partypes
    
    def is_function(self):
        return True
    def is_callable(self):
        return True
    
    def is_same_type(self,other):
        if not other.is_function():
            return False
        return other.return_type().is_same_type(self.return_type) and other.param_types.is_same_type(self.param_types)

    def is_compatible(self,target):
        if not target.is_function():
            return False
        return other.return_type().is_compatible(self.return_type) and other.param_types().is_same_type(self.param_types)

    def is_castable_to(self,target):
        return target.is_function()
    
    def return_type(self):
        return self.return_type

    def is_vararg(self):
        return self.param_types.is_vararg()
    
    def accepts_argc(self,num_args):
        if self.param_types.is_vararg():
            return num_args >= self.param_types.min_argc()
        else:
            return num_args == self.param_types.argc()
    
    def param_types(self):
        return self.param_types.types()
    
    def alignment(self):
        raise Exception("FunctionType.alignment called")
    
    def size(self):
        raise Exception("FunctionType.size called")
    
    def to_string(self):
        sep = ""
        buf = ""
        buf += self.return_type.to_string()
        buf += "("
        for t in self.param_types.types():
            buf += sep
            buf += t.to_string()
            sep = ", "
        buf += ")"
        return buf
               