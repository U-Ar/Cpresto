from type.Type import *
from type.TypeRef import *
from .Node import Node

class TypeNode(Node):
    def __init__(self,ref):
        super().__init__()
        if isinstance(ref,TypeRef):
            self._type_ref = ref
            self._type = None
        elif isinstance(ref,Type):
            self._type_ref = None
            self._type = ref
    
    def type_ref(self):
        return self._type_ref
    
    def is_resolved(self):
        return self._type != None
    
    def set_type(self,t):
        if self._type != None:
            raise Exception("TypeNode.set_type called twice")
        self._type = t
    
    def type(self):
        if self._type == None:
            raise Exception("TypeNode not resolved: "+ self._type_ref)
        return self._type
    
    def location(self):
        return (None if self._type_ref==None else self._type_ref.location())
    
    def _dump(self,dumper):
        dumper.print_member("typeref",self._type_ref)
        dumper.print_member("type",self._type)
    
    def accept(self,visitor):
        raise Exception("do not call TypeNode.accept")
