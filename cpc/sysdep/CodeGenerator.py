from abc import ABCMeta,abstractmethod

class CodeGenerator(metaclass=ABCMeta):
    @abstractmethod
    def generate(self,ir):
        pass