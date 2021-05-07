from abc import ABCMeta, abstractmethod
from .Node import Node

class StmtNode(Node):
    def __init__(self,loc):
        self._location = loc
    
    def location(self):
        return self._location
    
    @abstractmethod
    def accept(self,visitor):
        pass