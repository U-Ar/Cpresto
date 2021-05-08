from abc import abstractmethod

class Stmt(IRDumpable):
    def __init__(self,loc):
        self._location = loc

    @abstractmethod
    def accept(self,visitor):
        pass
    
    def location(self):
        return self._location
    
    def dump(self,dumper):
        dumper.print_class(self,self._location)
        self._dump(dumper)
    
    @abstractmethod
    def _dump(self,dumper):
        pass