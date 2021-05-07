from .Node import Node
from type.Type import Type

class Slot(Node):
    def __init__(self,t,n):
        self.type_node = t
        self.name = n
        self.offset = Type.size_unknown
    
    def type_node(self):
        return self.type_node
    
    def type_ref(self):
        return self.type_node.type_ref()
    
    def type(self):
        return self.type_node.type()
    
    def name(self):
        return self.name
    
    def size(self):
        return self.type().size()
    
    def alloc_size(self):
        return self.type().alloc_size()

    def alignment(self):
        return self.type().alignment()
    
    def offset(self):
        return self.offset
    
    def set_offset(self,offset):
        self.offset = offset
    
    def location(self):
        return self.type_node.location()
    
    def _dump(self,dumper):
        dumper.print_member("name",self.name)
        dumper.print_member("type_node",self.type_node)