from .ParamSlots import ParamSlots
from abst.Dumpable import Dumpable
import type

class Params(ParamSlots,Dumpable):
    def __init__(self,loc,param_descs):
        super().__init__(loc,param_descs,False)
    
    def parameters(self):
        return self.param_descriptors

    def parameters_type_ref(self):
        typerefs = []
        for param in self.param_descriptors:
            typerefs.append(param.type_node.type_ref)
        return ParamTypeRefs(self.location,self.typerefs,self.vararg)
    
    def equals(self,other):
        return isinstance(other,Params) and \
            other.vararg == self.vararg and \
                other.param_descriptors.equals(self.param_descriptors)
    
    def dump(self,dumper):
        dumper.print_node_list("parameters", self.parameters())
