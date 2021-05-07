from .Variable import Variable

class UndefinedVariable(Variable):
    def __init__(self,t,name):
        super().__init__(False,t,name)
    
    def is_defined(self):
        return False
    def is_private(self):
        return False
    def is_initialized(self):
        return False
    
    def _dump(self,dumper):
        dumper.print_member("name",self.name())
        dumper.print_member("is_private",self.is_private())
        dumper.print_member("type_node",self.type_node())
    
    def accept(self,visitor):
        return visitor.visit(self)