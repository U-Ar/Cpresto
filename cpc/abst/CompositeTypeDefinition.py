from abc import abstractmethod
from .TypeDefinition import TypeDefinition

class CompositeTypeDefinition(TypeDefinition):
    def __init__(self,loc,ref,name,membs):
        super().__init__(loc,ref,name)
        self.members = membs
    
    def is_composite_type(self):
        return True
    
    @abstractmethod
    def kind(self):
        pass

    def members(self):
        return self.members
    
    def _dump(self,dumper):
        dumper.print_member("name",name)
        dumper.print_node_list("members",members)