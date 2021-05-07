from abc import ABCMeta, abstractmethod

class Literal(metaclass=ABCMeta):
    @abstractmethod
    def to_source(self,table=None):
        pass
    
    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def collect_statistics(self,stats):
        pass

    @abstractmethod
    def is_zero(self):
        pass

    @abstractmethod
    def plus(self,diff):
        pass

    @abstractmethod
    def cmp(self,sym):
        pass
