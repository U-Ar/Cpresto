from .Node import Node
from type.Type import Type

class Slot(Node):
    def __init__(self,t,n):
        self._type_node = t
        self._name = n
        self._offset = Type.size_unknown
    
    def type_node(self):
        return self._type_node
    
    def type_ref(self):
        return self._type_node.type_ref()
    
    def type(self):
        return self._type_node.type()
    
    def name(self):
        return self._name
    
    def size(self):
        return self.type().size()
    
    def alloc_size(self):
        return self.type().alloc_size()

    def alignment(self):
        return self.type().alignment()
    
    def offset(self):
        return self._offset
    
    def set_offset(self,offset):
        self._offset = offset
    
    def location(self):
        return self._type_node.location()
    
    def _dump(self,dumper):
        dumper.print_member("name",self._name)
        dumper.print_member("type_node",self._type_node)