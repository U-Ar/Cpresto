from .Entity import Entity

class Constant(Entity):
    def __init__(self,t,name,value):
        super().__init__(True,t,name)
        self.value = value
    
    def is_assignable(self):
        return False
    def is_defined(self):
        return True
    def is_initialized(self):
        return True
    def is_constant(self):
        return True

    def value(self):
        return self.value
    
    def _dump(self,dumper):
        dumper.print_member("name", self.name)
        dumper.print_member("type_node",self.type_node)
        dumper.print_member("value",self.value)
    
    def accept(self,visitor):
        return visitor.visit(self)
