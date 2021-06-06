import sys
from abc import ABCMeta, abstractmethod
from .Dumper import Dumper

class Node(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def location(self):
        pass

    #def dump(self,ostream):
    #    dump(ostream)

    def dump(self,dumper=None):
        if dumper == None:
            self.dump(sys.stdout)
        else:
            op = getattr(dumper, "print_class", None)
            if callable(op):
                dumper.print_class(self,self.location())
                self._dump(dumper)
            else:
                self.dump(Dumper(dumper))
    
    @abstractmethod
    def _dump(self,dumper):
        pass
