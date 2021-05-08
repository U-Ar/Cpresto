#from abc import ABCMeta, abstractmethod

class TypeRef:#(metaclass=ABCMeta):
    def __init__(self,loc):
        self._location = loc
    
    def location(self):
        return self._location
    
    def hash_code(self):
        return self.to_string()