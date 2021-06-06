class Declarations:
    def __init__(self):
        self._defvars = set()
        self._vardecls = set()
        self._defuns = set()
        self._funcdecls = set()
        self._constants = set()
        self._defstructs = set()
        self._defunions = set()
        self._typedefs = set()
    
    def add(self,decls):
        self._defvars = self._defvars | set(decls.defvars())
        self._vardecls = self._vardecls | set(decls.vardecls())
        self._funcdecls = self._funcdecls | set(decls.funcdecls())
        self._constants = self._constants | set(decls.constants())
        self._defstructs = self._defstructs | set(decls.defstructs())
        self._defunions = self._defunions | set(decls.defunions())
        self._typedefs = self._typedefs | set(decls.typedefs())

    def add_defvar(self,var):
        self._defvars.add(var)
    
    def add_defvars(self,vs):
        for v in vs:
            self._defvars.add(v)
    
    def defvars(self):
        return list(self._defvars)
    
    def add_vardecl(self,var):
        self._vardecls.add(var)
    
    def vardecls(self):
        return list(self._vardecls)
    
    def add_constant(self,c):
        self._constants.add(c)
    
    def constants(self):
        return list(self._constants)
    
    def add_defun(self,fun):
        self._defuns.add(fun)
    
    def defuns(self):
        return list(self._defuns)
    
    def add_funcdecl(self,fun):
        self._funcdecls.add(fun)
    
    def funcdecls(self):
        return list(self._funcdecls)
    
    def add_defstruct(self,n):
        self._defstructs.add(n)
    
    def defstructs(self):
        return list(self._defstructs)
    
    def add_defunion(self,n):
        self._defunions.add(n)
    
    def defunions(self):
        return list(self._defunions)
    
    def add_typedef(self,n):
        self._typedefs.add(n)
    
    def typedefs(self):
        return list(self._typedefs)