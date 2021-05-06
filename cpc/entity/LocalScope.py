from Scope import Scope
from DefinedVariable import DefinedVariable

class LocalScope(Scope):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.parent.add_child(self)
        self.variables = dict()
    
    def is_toplevel(self):
        return False
    
    def toplevel(self):
        return self.parent.toplevel()

    def parent(self):
        return self.parent
    
    def children(self):
        return self.children
    
    def is_defined_locally(self,name):
        return name in self.variables
    
    # define variable in this scope.
    def define_variable(self,var):
        if var.name() in self.variables:
            raise Exception("duplicated variable: "+var.name())
        self.variables[var.name()] = var
    
    def allocate_tmp(self,t):
        var = DefinedVariable.tmp(t)
        self.define_variable(var)
        return var
    
    def get(self,name):
        if name in self.variables:
            return self.variables[name]
        else :
            return self.parent.get(name)
    
    # returns all local variables in this scope.
    # the result DOES include all nested local variables
    # it does NOT include static local variables
    def all_local_variables(self):
        result = []
        for s in self.all_local_scopes:
            result += s.local_variables()
        return result
    
    # return local variables defined in this scope
    # does NOT include children's local
    # does NOT include static local
    def local_variables(self):
        result = []
        for var in self.variables.values():
            if not var.is_private():
                result.append(var)
        return result
    
    # returns all static local defined in this scope
    def static_local_variables(self):
        result = []
        for s in self.all_local_scopes():
            for var in s.variables.values():
                if var.is_private():
                    result.append(var)
        return result
    
    # returns a list of all child scopes
    def all_local_scopes(self):
        result = []
        self.collect_scope(result)
        return result
    
    def collect_scope(self,buf):
        buf.append(self)
        for s in self.children:
            s.collect_scope(buf)
        
    def check_references(self,h):
        for var in self.variables.values():
            if not var.is_refered():
                h.warn("unused variable: "+var.name(),var.location())
        for c in self.children:
            c.check_references(h)