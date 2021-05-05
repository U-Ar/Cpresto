import sys
from abc import ABCMeta, abstractmethod

class Node(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def location(self):
        pass

    def dump(self):
        dump(sys.stdout)
    
    def dump(self,ostream):
        dump(ostream)
    
    def dump(self,dumper):
        dumper.print_class(self,self.location())
        self._dump()
    
    @abstractmethod
    def _dump(self,dumper):
        pass
