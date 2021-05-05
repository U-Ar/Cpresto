class Declarations:
    def __init__(self):
        self.defvars = set()
        self.vardecls = set()
        self.defuns = set()
        self.funcdecls = set()
        self.constants = set()
        self.defstructs = set()
        self.defunions = set()
        self.typedefs = set()
    
    def add(self,decls):
        self.defvars = self.defvars | decls.defvars
        self.vardecls = self.vardecls | decls.vardecls
        self.funcdecls = self.funcdecls | decls.funcdecls
        self.constants = self.constants | decls.constants
        self.defstructs = self.defstructs | decls.defstructs
        self.defunions = self.defunions | decls.defunions
        self.typedefs = self.typedefs | decls.typedefs

    def add_defvar(self,var):
        self.defvars.add(var)
    
    def add_defvars(self,vs):
        for v in vs:
            self.defvars.add(v)
    
    def defvars(self):
        return list(self.defvars)
    
    def add_vardecl(self,var):
        self.vardecls.add(var)
    
    def vardecls(self):
        return list(self.vardecls)
    
    def add_constant(self,c):
        self.constants.add(c)
    
    def constants(self):
        return list(self.constants)
    
    def add_defun(self,fun):
        self.defuns.add(fun)
    
    def defuns(self):
        return list(self.defuns)
    
    def add_funcdecl(self,fun):
        self.funcdecls.add(fun)
    
    def funcdecls(self):
        return list(self.funcdecls)
    
    def add_defstruct(self,n):
        self.defstructs.add(n)
    
    def defstructs(self):
        return list(self.defstructs)
    
    def add_defunion(self,n):
        self.defunions.add(n)
    
    def defunions(self):
        return list(self.defunions)
    
    def add_typedef(self,n):
        self.typedefs.add(n)
    
    def typedefs(self):
        return list(self.typedefs)