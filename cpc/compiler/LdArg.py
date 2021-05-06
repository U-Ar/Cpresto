from abc import ABCMeta, abstractmethod

class LdArg(metaclass=ABCMeta):
    def __init__(self):
        pass
    @abstractmethod
    def to_string(self):
        pass
    @abstractmethod
    def is_source_file(self):
        pass
