from abc import ABCMeta, abstractmethod
from .Literal import Literal

class Symbol(Literal):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def to_string(self):
        pass

    @abstractmethod
    def dump(self):
        pass
    