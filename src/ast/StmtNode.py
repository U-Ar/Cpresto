from abc import ABCMeta, abstractmethod

class StmtNode(Node):
    def __init__(self,loc):
        self.location = loc
    
    def location(self):
        return self.location
    
    @abstractmethod
    def accept(self,visitor):
        pass