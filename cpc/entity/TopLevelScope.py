from .Scope import Scope
from .Variable import Variable
from .DefinedVariable import DefinedVariable
import exception

class ToplevelScope(Scope):
    def __init__(self):
        super().__init__()
        self.entities = dict()
        self._static_local_variables = None
    
    def is_toplevel(self):
        return True
    
    def toplevel(self):
        return self
    
    def parent(self):
        return None
    
    # declare variable or function globally
    def declare_entity(self,entity):
        if entity.name() in self.entities:
            e = self.entities[entity.name()]
            raise SemanticException("duplicated declaration: "+ \
                entity.name() + ": " + e.location() + \
                    " and " + entity.location())
        self.entities[entity.name()] = entity
    
    # define variable or function globally
    def define_entity(self,entity):
        if entity.name() in self.entities:
            e = self.entities[entity.name()]
            if e.is_defined():
                raise SemanticException("duplicated definition: "+ \
                    entity.name() + ": " + e.location() + \
                        " and " + entity.location())
        self.entities[entity.name()] = entity

    # searches and gets entity searching scopes upto toplevelscope
    def get(self,name):
        if name in self.entities:
            return self.entities[name]
        else :
            raise SemanticException("unresolved reference: " + name)

    # returns a list of all global variables
    def all_global_variables(self):
        result = []
        for ent in self.entities.values():
            if isinstance(ent,Variable):
                result.append(ent)
        result += self.static_local_variables()
        return result
    
    def defined_global_scope_variables(self):
        result = []
        for ent in self.entities.values():
            if isinstance(ent,DefinedVariable):
                result.append(ent)
        result += self.static_local_variables()
        return result
    
    def static_local_variables(self):
        if self._static_local_variables == None:
            self._static_local_variables = []
            for s in self.children:
                self._static_local_variables += s.static_local_variables()
            seq_table = dict()
            for var in self._static_local_variables:
                if var.name() not in seq_table:
                    var.set_sequence(0)
                    seq_table[var.name()] = 1
                else :
                    seq = seq_table[var.name()]
                    var.set_sequence(seq)
                    seq_table[var.name()] = seq + 1
        return self._static_local_variables
    
    def check_references(self,h):
        for ent in self.entities.values():
            if ent.is_defined() and ent.is_private() and \
                not ent.is_constant() and not ent.is_refered():
                h.warn("unused variable: " + ent.name())
        
        for func_scope in self.children:
            for s in func_scope.children:
                s.check_references(h)
