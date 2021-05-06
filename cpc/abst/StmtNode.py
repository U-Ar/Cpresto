from abc import ABCMeta, abstractmethod
from .Node import Node

class StmtNode(Node):
    def __init__(self,loc):
        self.location = loc
    
    def location(self):
        return self.location
    
    @abstractmethod
    def accept(self,visitor):
        pass