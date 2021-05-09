from abc import ABCMeta,abstractmethod
from .Operand import Operand

class MemoryReference(Operand,metaclass=ABCMeta):
    def is_memory_reference(self):
        return True
        
    @abstractmethod
    def fix_offset(self,diff):
        pass

    @abstractmethod
    def cmp(self,mem):
        pass