from abc import ABCMeta,abstractmethod

class Scope(metaclass=ABCMeta):
    def __init__(self):
        self.children = []
    
    @abstractmethod
    def is_toplevel(self):
        pass

    @abstractmethod
    def toplevel(self):
        pass

    @abstractmethod
    def parent(self):
        pass

    def add_child(self,s):
        self.children.append(s)
    
    @abstractmethod
    def get(self,name):
        pass