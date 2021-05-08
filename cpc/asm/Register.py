from abc import ABCMeta,abstractmethod
from .Operand import Operand

class Register(Operand):
    def is_register(self):
        return True

    def collect_statistics(self,stats):
        stats.register_used(self)
    
    @abstractmethod
    def to_source(self,syms):
        pass

    @abstractmethod
    def dump(self):
        pass