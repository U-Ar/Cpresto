from abc import ABCMeta,abstractmethod

class AssemblyCode(metaclass=ABCMeta):
    @abstractmethod
    def to_source(self):
        pass

    @abstractmethod
    def dump(self,s=None):
        pass
