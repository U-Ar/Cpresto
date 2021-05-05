from ..exception.SemanticError import SemanticError

class PtrMemberNode(LHSNode):
    def __init__(self,expr,member):
        self.expr = expr
        self.member = member
    
    def derefered_composite_type(self):
        try:
            pt = self.expr.type().get_pointer_type()
            return pt.base_type().get_composite_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def derefered_type(self):
        try:
            pt = self.expr.type().get_pointer_type()
            return pt.base_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def expr(self):
        return self.expr
    
    def member(self):
        return self.member
    
    def offset(self):
        return self.derefered_composite_type().member_offset(self.member)
    
    def orig_type(self):
        return self.derefered_composite_type().member_type(self.member)
    
    def location(self):
        return self.expr.location()
    
    def _dump(self,dumper):
        if self.type != None:
            dumper.print_member("type",self.type)
        dumper.print_member("expr",self.expr)
        dumper.print_member("member",self.member)
    
    def accept(self,visitor):
        return visitor.visit(self)