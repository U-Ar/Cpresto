from type.Type import *
from type.TypeRef import *
from .Node import Node

class TypeNode(Node):
    def __init__(self,ref):
        super().__init__()
        if isinstance(ref,TypeRef):
            self.type_ref = ref
            self.type = None
        elif isinstance(ref,Type):
            self.type_ref = None
            self.type = ref
    
    def type_ref(self):
        return self.type_ref
    
    def is_resolved(self):
        return self.type != None
    
    def set_type(self,t):
        if self.type != None:
            raise Exception("TypeNode.set_type called twice")
        self.type = t
    
    def type(self):
        if self.type == None:
            raise Exception("TypeNode not resolved: "+ self.type_ref)
        return self.type
    
    def location(self):
        return (None if self.type_ref==None else self.type_ref.location)
    
    def _dump(self,dumper):
        dumper.print_member("typeref",self.type_ref)
        dumper.print_member("type",self.type)
    
    def accept(self,visitor):
        raise Exception("do not call TypeNode.accept")
