from .Variable import Variable
import abst

class DefinedVariable(Variable):

    def __init__(self,priv,t,name,init):
        super().__init__(priv,t,name)
        self.initializer = init
        self.sequence = -1
        self.ir = None
        self.symbol = None
    
    tmp_seq = 0

    @staticmethod
    def tmp(t):
        DefinedVariable.tmp_seq += 1
        return DefinedVariable(False,
                TypeNode(t), "@tmp"+DefinedVariable.tmp_seq-1,None)
    
    def is_defined(self):
        return True
    
    def set_sequence(self,seq):
        self.sequence = seq
    
    def symbol_string(self):
        if self.sequence < 0:
            return self.name
        else :
            return self.name + "." + str(self.sequence)
    
    def has_initializer(self):
        return self.initializer != None

    def is_initialized(self):
        return self.has_initialier()
    
    def initializer(self):
        return self.initializer

    def set_initializer(self,expr):
        self.initializer = expr
    
    def set_IR(self,expr):
        self.ir = expr
    
    def ir(self):
        return self.ir
    
    def _dump(self,dumper):
        dumper.print_member("name", self.name)
        dumper.print_member("is_private", self.is_private)
        dumper.print_member("type_node", self.type_node)
        dumper.print_member("initializer", self.initializer)
    
    def accept(self,visitor):
        return visitor.visit(self)