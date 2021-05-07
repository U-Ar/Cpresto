from .TypeNode import TypeNode
from .Node import Node
from abc import ABCMeta, abstractmethod

class TypeDefinition(Node):
    def __init__(self,loc,ref,name):
        self.name = name
        self.location = loc
        self.type_node = TypeNode(ref)
    
    def name(self):
        return self.name

    def location(self):
        return self.location
    
    def type_node(self):
        return self.type_node
    
    def type_ref(self):
        return self.type_node.type_ref()
    
    def type(self):
        return self.type_node.type()

    @abstractmethod
    def defining_type(self):
        pass

    @abstractmethod
    def accept(self,visitor):
        pass
    
    