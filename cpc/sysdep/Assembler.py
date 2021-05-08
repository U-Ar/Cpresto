from abc import ABCMeta,abstractmethod

class Assembler(metaclass=ABCMeta):
    @abstractmethod
    def assemble(self,srcpath,destpath,opts):
        pass