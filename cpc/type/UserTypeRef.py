from TypeRef import TypeRef
from UserTypeRef import UserTypeRef

class UserTypeRef(TypeRef):
    def __init__(self,name,loc=None):
        super().__init__(loc)
        self.name = name
    
    def is_user_type(self):
        return True
    
    def name(self):
        return self.name
    
    def equals(self,other):
        if not isinstance(other,UserTypeRef):
            return False
        return self.name == other.name
    
    def to_string(self):
        return self.name