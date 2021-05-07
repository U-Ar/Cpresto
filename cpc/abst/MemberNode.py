from exception.SemanticError import SemanticError
from .LHSNode import LHSNode

class MemberNode(LHSNode):
    def __init__(self,expr,member):
        self.expr = expr
        self.member = member
    
    def base_type(self):
        try:
            return self.expr.type().get_composite_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def expr(self):
        return self.expr
    
    def member(self):
        return self.member
    
    def offset(self):
        return self.base_type.member_offset(self.member)
    
    def orig_type(self):
        return self.base_type.member_type(self.member)
    
    def location(self):
        return self.expr.location()
    
    def _dump(self,dumper):
        if self.type != None:
            dumper.print_member("type",self.type)
        dumper.print_member("expr",self.expr)
        dumper.print_member("member",self.member)
    
    def accept(self,visitor):
        return visitor.visit(self)