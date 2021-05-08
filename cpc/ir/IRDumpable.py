from abc import ABCMeta, abstractmethod

class IRDumpable(metaclass=ABCMeta):
    @abstractmethod
    def dump(self,dumper):
        pass