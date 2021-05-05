from abc import ABCMeta, abstractmethod

class Dumpable(metaclass=ABCMeta):
    @abstractmethod
    def dump(self,dumper):
        pass