from type.UserTypeRef import UserTypeRef
from type.UserType import UserType
from .TypeNode import TypeNode
from .TypeDefinition import TypeDefinition

class TypedefNode(TypeDefinition):
    def __init__(self,loc,real,name):
        super().__init__(loc,UserTypeRef(name),name)
        self.real = TypeNode(real)
    
    def is_user_type(self):
        return True
    
    def real_type_node(self):
        return self.real
    
    def real_type(self):
        return self.real.type()
    
    def real_type_ref(self):
        return self.real.type_ref()
    
    def defining_type(self):
        return UserType(self.name(),self.real_type_node(),self.location())
    
    def _dump(self,dumper):
        dumper.print_member("name",self.name())
        dumper.print_member("type_node",self.type_node())
    
    def accept(self,visitor):
        return visitor.visit(self)