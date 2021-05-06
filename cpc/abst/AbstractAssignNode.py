class AbstractAssignNode(ExprNode):
    def __init__(self,lhs,rhs):
        super().__init__()
        self.lhs=lhs
        self.rhs=rhs
    
    def type(self):
        return self.lhs.type()
    
    def lhs(self):
        return self.lhs
    
    def rhs(self):
        return self.rhs
    
    def set_rhs(self,expr):
        self.rhs = expr
    
    def location(self):
        return self.lhs.location()
    
    def _dump(self,dumper):
        dumper.print_member("lhs",self.lhs)
        dumper.print_member("rhs",self.rhs)
