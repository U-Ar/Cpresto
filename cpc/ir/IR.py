import sys
from .IRDumper import IRDumper

class IR:
    def __init__(self,source,defvars,defuns,funcdecls,scope,constant_table):
        self.source = source
        self.defvars = defvars
        self.defuns = defuns
        self.funcdecls = funcdecls
        self.scope = scope
        self.constant_table = constant_table
        self.comms = None
        self.gvars = None
    
    def file_name(self):
        return self.source.source_name()
    
    def location(self):
        return self.source
    
    def defined_variables(self):
        return self.defvars

    def is_function_defined(self):
        return not self.defuns.is_empty()

    def defined_functions(self):
        return self.defuns
    
    def scope(self):
        return self.scope

    def all_functions(self):
        res = []
        res += self.defuns
        res += self.funcdecls
        return res
    
    def all_global_variables(self):
        return self.scope.all_global_variables()

    def is_global_variable_defined(self):
        return len(self.defined_global_variables()) > 0
    
    def defined_global_variables(self):
        if self.gvars == None:
            self.init_variables()
        return self.gvars
    
    def is_common_symbol_defined(self):
        return len(self.defined_common_symbols) > 0
    
    def defined_common_symbols(self):
        if self.comms = None:
            self.init_variables()
        return self.comms
    
    def init_variables(self):
        self.gvars = []
        self.comms = []
        for var in self.scope.defined_global_scope_variables():
            if var.has_initializer():
                self.gvars.append(var)
            else :
                self.comms.append(var)
    
    def is_string_literal_defined(self):
        return not self.constant_table.is_empty()
    
    def constant_table(self):
        return self.constant_table

    def dump(self,s=None):
        if s = None:
            s = sys.stdout
        d = IRDumper(s)
        d.print_class(self,self.source)
        d.print_vars("variables",self.defvars)
        d.print_funcs("functions",self.defuns)