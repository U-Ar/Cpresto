from .CompositeTypeDefinition import CompositeTypeDefinition
from ..type.UnionType import UnionType

class UnionNOde(CompositeTypeDefinition):
    def __init__(self,loc,ref,name,membs):
        super().__init__(loc,ref,name,membs)
    
    def kind(self):
        return "union"
    
    def is_union(self):
        return True
    
    def defining_type(self):
        return UnionType(self.name(),self.members(),self.location())
    
    def accept(self, visitor):
        return visitor.visit(self)