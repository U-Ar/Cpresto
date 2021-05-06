from ..entity.ParamSlots import ParamSlots

class ParamTypes(ParamSlots):
    def __init__(self,param_descs,loc,vararg):
        super().__init__(param_descs,loc,vararg)
    
    def types(self):
        return self.param_descriptors
    
    def is_same_type(self, other):
        if self.vararg != other.vararg:
            return False
        if self.min_argc() != other.min_argc():
            return False
        for t,o in zip(self.param_descriptors,other.types()):
            if not t.is_same_type(o):
                return False
        return True
    
    def equals(self,other):
        if not isinstance(other,ParamTypes):
            return False
        if self.vararg != other.vararg:
            return False
        if len(self.param_descriptors) != len(other.types()):
            return False
        for t,o in zip(self.param_descriptors,other.types()):
            if not t.equals(o):
                return False
        return True
        