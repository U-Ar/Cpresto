from abc import abstractmethod

class Expr(IRDumpable):
    def __init__(self,t):
        self._type = t
    
    def type(self):
        return self._type

    def is_var(self):
        return False
    
    def is_addr(self):
        return False
    
    def is_constant(self):
        return False
    
    def asm_value(self):
        raise Exception("Expr.asm_value called")
    
    def address(self):
        raise Exception("Expr.address called")
    
    def memref(self):
        raise Exception("Expr.memref called")
    
    def address_node(self,t):
        raise Exception("unexpected node for LHS: " + str(type(self)))
    
    def get_entity_force(self):
        return None
    
    @abstractmethod
    def accept(self,visitor):
        pass

    def dump(self,dumper):
        dumper.print_class(self)
        dumper.print_member("type",self._type)
        self._dump(dumper)
    
    @abstractmethod
    def _dump(self,dumper):
        pass
