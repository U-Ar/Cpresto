from abc import ABCMeta,abstractmethod
from ..ast.Dumpable import Dumpable

class Entity(Dumpable,metaclass=ABCMeta):
    def __init__(self,priv,t,name):
        self.name = name
        self.is_private = priv
        self.type_node = t
        self.n_refered = 0
        self.memref = None
        self.address = None
    
    def name(self):
        return self.name
    
    def symbol_string(self):
        return self.name()
    
    @abstractmethod
    def is_defined(self):
        pass

    @abstractmethod
    def is_initialized(self):
        pass

    def is_constant(self):
        return False
    
    def value(self):
        raise Exception("Entity.value()")
    
    def is_parameter(self):
        return False
    
    def is_private(self):
        return self.is_private
    
    def type_node(self):
        return self.type_node

    def type(self):
        return self.type_node.type()

    def alloc_size(self):
        return self.type().alloc_size()

    def alignment(self):
        return self.type().alignment()
    
    def refered(self):
        self.n_refered += 1
    
    def is_refered(self):
        return self.n_refered > 0
    
    def set_memref(self,mem):
        self.memref = mem
    
    def memref(self):
        self.check_address()
        return self.memref
    
    def set_address(self,mem):
        self.address = mem
    
    def address(self):
        self.check_address():
        return self.address
    
    def check_address(self):
        if self.memref == None and self.address = None:
            raise Exception("address did not resolved: "+self.name)
    
    def location(self):
        return self.type_node.location()
    
    @abstractmethod
    def accept(self,visitor):
        pass

    def dump(self,dumper):
        dumper.print_class(self,self.location())
        self._dump(dumper)
    
    @abstractmethod
    def _dump(self,dumper):
        pass