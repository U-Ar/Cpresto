from abc import ABCMeta,abstractmethod

class Platform(metaclass=ABCMeta):
    @abstractmethod
    def type_table(self):
        pass

    @abstractmethod
    def code_generator(self,opts,h):
        pass

    @abstractmethod
    def assembler(self,h):
        pass

    @abstractmethod
    def linker(self,h):
        pass