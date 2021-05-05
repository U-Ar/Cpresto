from .Type import Type

class NamedType(Type):
    def __init__(self,name,loc):
        self.name = name
        self.location = loc
    
    def name(self):
        return self.name
    
    def location(self):
        return self.location