from .LHSNode import LHSNode
from exception.SemanticError import SemanticError

class PtrMemberNode(LHSNode):
    def __init__(self,expr,member):
        self._expr = expr
        self._member = member
    
    def derefered_composite_type(self):
        try:
            pt = self._expr.type().get_pointer_type()
            return pt.base_type().get_composite_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def derefered_type(self):
        try:
            pt = self._expr.type().get_pointer_type()
            return pt.base_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def expr(self):
        return self._expr
    
    def member(self):
        return self._member
    
    def offset(self):
        return self.derefered_composite_type().member_offset(self._member)
    
    def orig_type(self):
        return self.derefered_composite_type().member_type(self._member)
    
    def location(self):
        return self._expr.location()
    
    def _dump(self,dumper):
        if self.type != None:
            dumper.print_member("type",self.type())
        dumper.print_member("expr",self._expr)
        dumper.print_member("member",self._member)
    
    def accept(self,visitor):
        return visitor.visit(self)