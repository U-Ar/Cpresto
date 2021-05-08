from .ParamSlots import ParamSlots
from abst.Dumpable import Dumpable
from type.ParamTypeRefs import ParamTypeRefs

class Params(ParamSlots,Dumpable):
    def __init__(self,loc,param_descs):
        super().__init__(param_descs,loc,False)
    
    def parameters(self):
        return self.param_descriptors

    def parameters_type_ref(self):
        typerefs = []
        #print("type of self.param_desc",type(self.param_descriptors))
        for param in self.param_descriptors:
            typerefs.append(param.type_node().type_ref)
        return ParamTypeRefs(self.location(),typerefs,self.vararg)
    
    def equals(self,other):
        return isinstance(other,Params) and \
            other.vararg == self.vararg and \
                other.param_descriptors.equals(self.param_descriptors)
    
    def dump(self,dumper):
        dumper.print_node_list("parameters", self.parameters())
