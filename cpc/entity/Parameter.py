from .DefinedVariable import DefinedVariable

class Parameter(DefinedVariable):
    def __init__(self,t,name):
        super().__init__(False,t,name,None)
    
    def is_parameter(self):
        return True
    
    def _dump(self,dumper):
        dumper.print_member("name",self.name)
        dumper.print_member("type_node",self.type_node)