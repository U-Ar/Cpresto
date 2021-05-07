from abc import ABCMeta,abstractmethod
from abst.Dumpable import Dumpable

class Entity(Dumpable):
    def __init__(self,priv,t,name):
        self._name = name
        self._is_private = priv
        self._type_node = t
        self.n_refered = 0
        self._memref = None
        self._address = None
    
    def name(self):
        return self._name
    
    def symbol_string(self):
        return self._name
    
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
        return self._is_private
    
    def type_node(self):
        return self._type_node

    def type(self):
        return self._type_node.type()

    def alloc_size(self):
        return self.type().alloc_size()

    def alignment(self):
        return self.type().alignment()
    
    def refered(self):
        self.n_refered += 1
    
    def is_refered(self):
        return self.n_refered > 0
    
    def set_memref(self,mem):
        self._memref = mem
    
    def memref(self):
        self.check_address()
        return self._memref
    
    def set_address(self,mem):
        self._address = mem
    
    def address(self):
        self.check_address()
        return self._address
    
    def check_address(self):
        if self._memref == None and self._address == None:
            raise Exception("address did not resolved: "+self._name)
    
    def location(self):
        return self._type_node.location()
    
    @abstractmethod
    def accept(self,visitor):
        pass

    def dump(self,dumper):
        dumper.print_class(self,self.location())
        self._dump(dumper)
    
    @abstractmethod
    def _dump(self,dumper):
        pass