from .Expr import Expr

class Str(Expr):
    def __init__(self,t,entry):
        super().__init__(t)
        self._entry = entry

    def entry(self):
        return self._entry
    
    def symbol(self):
        return self._entry.symbol()
    
    def is_constant(self):
        return True
    
    def memref(self):
        return self._entry.memref()
    
    def address(self):
        return self._entry.address()
    
    def asm_value(self):
        return self._entry.address()
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("entry",self._entry.to_string())