class ParamSlots:
    def __init__(self,param_descs,loc=None,vararg=None):
        if vararg == None:
            self.vararg = False
        else:
            self.vararg = True
        self.param_descriptors = param_descs
        self.location = loc
    
    def argc(self):
        if self.vararg:
            raise Exception("must not hapen: Param.argc for vararg")
        return len(self.param_descriptors)
    
    def min_argc(self):
        return len(self.param_descriptors)
    
    def accept_varargs(self):
        self.vararg = True
    
    def is_vararg(self):
        return self.vararg
    
    def location(self):
        return self.location