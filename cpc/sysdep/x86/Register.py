import asm.Register
from asm.Type import Type
from .RegisterClass import RegisterClass

class Register(asm.Register):

    def __init__(self,cl,t):
        self._class = cl
        self._type = t
    
    def for_type(self,t):
        return Register(self._class,t)
    
    def type(self):
        return self._type
    
    def is_register(self):
        return True
    
    def equals(self,other):
        return isinstance(other,Register) and self._class.equals(other._class)
    
    def hash_code(self):
        return self._class.hash_code()

    def register_class(self):
        return self._class
    
    def base_name(self):
        return self._class.to_string().lower()

    def typed_name(self):
        if self._type == Type.INT8:
            return self.lower_byte_register()
        elif self._type == Type.INT16:
            return self.base_name()
        elif self._type == Type.INT32:
            return "e" + self.base_name()
        elif self._type == Type.INT64:
            return "r" + self.base_name()
        else :
            raise Exception("unknown register type: " + self._type)
    
    def lower_byte_register(self):
        if self._class == RegisterClass.AX:
            pass
        elif self._class == RegisterClass.BX:
            pass
        elif self._class == RegisterClass.CX:
            pass
        elif self._class == RegisterClass.DX:
            return self.base_name()[0:1] + "l"
        else :
            raise Exception("does not have lower-byte register: " + self._class)
        
    def dump(self):
        return "(Register " + self._class.to_string() + " " + self._type.to_string() + ")"