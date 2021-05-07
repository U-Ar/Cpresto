from .StmtNode import StmtNode

class IfNode(StmtNode):
    def __init__(self,loc,c,t,e):
        super().__init__(loc)
        self.cond = c
        self.then_body = t
        self.else_body = e
    
    def cond(self):
        return self.cond
    
    def then_body(self):
        return self.then_body
    
    def else_body(self):
        return self.else_body
    
    def _dump(self,dumper):
        dumper.print_member("cond",self.cond)
        dumper.print_member("then_body",self.then_body)
        dumper.print_member("else_body",self.else_body)
    
    def accept(self,visitor):
        return visitor.visit(self)