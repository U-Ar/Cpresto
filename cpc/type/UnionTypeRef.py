from .TypeRef import TypeRef

class UnionTypeRef(TypeRef):
    def __init__(self,name,loc=None):
        super().__init__(loc)
        self.name = name
    
    def is_union(self):
        return True
    
    def equals(self,other):
        if not isinstance(other,UnionTypeRef):
            return False
        return self.name == other.name()
    
    def name(self):
        return self.name
    
    def to_string(self):
        return "union " + self.name
