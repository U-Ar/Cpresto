from ..type.StructType import StructType

class StructNode(CompositeTypeDefinition):
    def __init__(self,loc,ref,name,membs):
        super().__init__(loc,ref,name,membs)
    
    def kind(self):
        return "struct"
    
    def is_struct(self):
        return True
    
    def defining_type(self):
        return StructType(self.name(),self.members(),self.location())
    
    def accept(self,visitor):
        return visitor.visit(self)