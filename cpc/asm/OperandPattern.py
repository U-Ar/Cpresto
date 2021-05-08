from abc import ABCMeta,abstractmethod

class OperandPattern(metaclass=ABCMeta):
    @abstractmethod
    def match(self,operand):
        pass