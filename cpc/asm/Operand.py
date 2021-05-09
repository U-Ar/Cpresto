from abc import ABCMeta, abstractmethod
from .OperandPattern import OperandPattern

class Operand(OperandPattern):
    @abstractmethod
    def to_source(self,table=None):
        pass
    @abstractmethod
    def dump(self):
        pass

    def is_register(self):
        return False

    def is_memory_reference(self):
        return False
    
    def integer_literal(self):
        return None

    @abstractmethod
    def collect_statistics(self,stats):
        pass

    def match(self,operand):
        return self is operand

    