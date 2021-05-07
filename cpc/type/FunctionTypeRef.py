from .TypeRef import TypeRef

class FunctionTypeRef(TypeRef):
    def __init__(self,return_type,params):
        super().__init__(return_type.location)
        self.return_type = return_type
        self.params = params
    
    def is_function(self):
        return True
    
    def equals(self,other):
        return isinstance(other,FunctionTypeRef) and \
            self.return_type.equals(other.return_type()) and \
                self.params.equals(other.params())
    
    def return_type(self):
        return self.return_type
    
    def params(self):
        return self.params
    
    def to_string(self):
        buf = self.return_type.to_string() + " ("
        sep = ""
        for ref in self.params.typerefs():
            buf += sep
            buf += ref.to_string()
            sep = ", "
        buf += ")"
        return buf