from .Expr import Expr

class Addr(Expr):
    def __init__(self,t,entity):
        super().__init__(t)
        self._entity = entity

    def is_addr(self):
        return True
    
    def entity(self):
        return self._entity
    
    def address(self):
        return self._entity.address()
    
    def memref(self):
        return self._entity.memref()
    
    def get_entity_force(self):
        return self._entity
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("entity",self._entity.name())