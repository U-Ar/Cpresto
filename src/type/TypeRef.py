from abc import ABCMeta, abstractmethod
from ..ast.Location import Location

class TypeRef(metaclass=ABCMeta):
    def __init__(self,loc):
        self.location = loc
    
    def location(self):
        return self.location
    
    def hash_code(self):
        return self.to_string()