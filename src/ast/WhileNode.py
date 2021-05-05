from .StmtNode import StmtNode

class WhileNode(StmtNode):
    def __init__(self,loc,cond,body):
        super().__init__(loc)
        self.cond = cond
        self.body = body
    
    def cond(self):
        return self.cond
    
    def body(self):
        return self.body
    
    def _dump(self,dumper):
        dumper.print_member("cond",self.cond)
        dumper.print_member("body",self.body)
    
    def accept(self,visitor):
        return visitor.visit(self)
