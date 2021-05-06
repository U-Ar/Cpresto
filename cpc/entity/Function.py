from .Entity import Entity
import asm

class Function(Entity):
    def __init__(self,priv,t,name):
        super().__init__(priv,t,name)
        self.calling_symbol = None
        self.label = None
    
    def is_initialized(self):
        return True
    
    @abstractmethod
    def is_defined(self):
        pass

    @abstractmethod
    def parameters(self):
        pass

    def return_type(self):
        return self.type().get_function_type().return_type()
    
    def is_void(self):
        return self.return_type().is_void()
    
    def set_calling_symbol(self,sym):
        if self.calling_symbol != None:
            raise Exception("must not happen: Function.calling_symbol set twice")
        self.calling_symbol = sym

    def calling_symbol(self):
        if self.calling_symbol == None:
            raise Exception("must not happen: Function.calling_symbol called but None")
        return self.calling_symbol

    def label(self):
        if self.label != None:
            return self.label
        else:
            return self.label = Label(self.calling_symbol())
    
