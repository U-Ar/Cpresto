from ..entity.ParamSlots import ParamSlots

class ParamTypeRefs(ParamSlots):
    def __init__(self,param_descs,loc=None,vararg=None):
        super().__init__(param_descs,loc,vararg)
    
    
    def typerefs(self):
        return self.param_descriptors
    
    def intern_types(self,table):
        types = []
        for ref in self.param_descriptors:
            types.append(table.get_param_type(ref))
        return ParamTypes(types,self.location,self.vararg)

    def equals(self,other):
        if not isinstance(other,ParamTypeRefs) or (self.vararg != other.vararg):
            return False
        if len(self.param_descriptors) != len(other.param_descriptors):
            return False
        for p,o in zip(self.param_descriptors,other.param_descriptors):
            if not p.equals(o):
                return False
        return True
        