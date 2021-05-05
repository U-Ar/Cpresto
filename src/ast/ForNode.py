from ..ExprStmtNode import ExprStmtNode

class ForNode(StmtNode):
    def __init__(self,loc,init,cond,incr,body):
        super().__init__(loc)
        self.init = ExprStmtNode(init.location(),init)
        self.cond = cond
        self.incr = ExprStmtNode(incr.location(),incr)
        self.body = body

    def init(self):
        return self.init
    
    def cond(self):
        return self.cond
    
    def incr(self):
        return self.incr
    
    def body(self):
        return self.body
    
    def _dump(self,dumper):
        dumper.print_member("init",self.init)
        dumper.print_member("cond",self.cond)
        dumper.print_member("incr",self.incr)
        dumper.print_member("body",self.body)
    
    def accept(self,visitor):
        return visitor.visit(self)