from .Expr import Expr
from .Addr import Addr

class Var(Expr):
    def __init__(self,t,entity):
        super().__init__(t)
        self._entity = entity
    
    def is_var(self):
        return True
    
    def type(self):
        if super().type() == None:
            raise Exception("Var is too big to load by 1 insn")
        return super().type()
    
    def name(self):
        return self._entity.name()
    def entity(self):
        return self._entity
    
    def address(self):
        return self._entity.address()
    
    def memref(self):
        return self._entity.memref()

    def address_node(self,t):
        return Addr(t,self._entity)
    
    def get_entity_force(self):
        return self._entity
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("entity",self._entity.name())