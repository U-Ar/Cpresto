from exception.SemanticError import SemanticError
from .LHSNode import LHSNode

class MemberNode(LHSNode):
    def __init__(self,expr,member):
        self._expr = expr
        self._member = member
    
    def base_type(self):
        try:
            return self._expr.type().get_composite_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def expr(self):
        return self._expr
    
    def member(self):
        return self._member
    
    def offset(self):
        return self.base_type.member_offset(self._member)
    
    def orig_type(self):
        return self.base_type.member_type(self._member)
    
    def location(self):
        return self._expr.location()
    
    def _dump(self,dumper):
        if self.type() != None:
            dumper.print_member("type",self.type())
        dumper.print_member("expr",self._expr)
        dumper.print_member("member",self._member)
    
    def accept(self,visitor):
        return visitor.visit(self)