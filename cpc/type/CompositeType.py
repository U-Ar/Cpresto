from .Type import Type
from .NamedType import NamedType
from ..exception.SemanticError import SemanticError
from abc import ABCMeta, abstractmethod

class CompositeType(NamedType):
    def __init__(self,name,membs,loc):
        super().__init__(name,loc)
        self.members = membs
        self.cached_size = Type.size_unknown
        self.cached_align = Type.size_unknown
        self.is_recursive_checked = False
    
    def is_composite_type(self):
        return True
    
    def is_same_type(self,other):
        if self.is_struct() and not other.is_struct():
            return False
        if self.is_union() and not other.is_union():
            return False
        #これいいの?
        if len(self.members) != len(other.members()):
            return False
        for t,o in zip(self.member_types(),other.member_types()):
            if not t.is_same_type(o):
                return False
        return True
    
    def is_compatible(self,other):
        if self.is_struct() and not other.is_struct():
            return False
        if self.is_union() and not other.is_union():
            return False
        #これいいの?
        if len(self.members) != len(other.members()):
            return False
        for t,o in zip(self.member_types(),other.member_types()):
            if not t.is_compatible(o):
                return False
        return True
    
    def is_castable_to(self,other):
        if self.is_struct() and not other.is_struct():
            return False
        if self.is_union() and not other.is_union():
            return False
        #これいいの?
        if len(self.members) != len(other.members()):
            return False
        for t,o in zip(self.member_types(),other.member_types()):
            if not t.is_castable_to(o):
                return False
        return True

    def size(self):
        if self.cached_size == Type.size_unknown:
            self.compute_offsets()
        return self.cached_size
    
    def alignment(self):
        if self.cached_align == Type.size_unknown:
            self.compute_offsets()
        return self.cached_align
    
    def members(self):
        return self.members
    
    def member_types(self):
        result = []
        for s in self.members:
            result.append(s.type())
        return result
    
    def has_member(self,name):
        return self.get(name) != None
    
    def member_type(self,name):
        return self.fetch(name).type()
    
    def member_offset(self,name):
        s = self.fetch(name)
        if s.offset() == Type.size_unknown:
            self.compute_offsets()
        return s.offset()
    
    @abstractmethod
    def compute_offsets(self):
        pass

    def fetch(self,name):
        s = self.get(name)
        if s == None:
            raise SemanticError("no such member in " + self.to_string() + ": " + name)
        return s

    def get(self,name):
        for s in self.members:
            if s.name().equals(name):
                return s
        return None

        
        
        

    