class DoWhileNode(StmtNode):
    def __init__(self,loc,body,cond):
        super().__init__(loc)
        self.body = body
        self.cond = cond
    
    def body(self):
        return self.body
    
    def cond(self):
        return self.cond
    
    def _dump(self,dumper):
        dumper.print_member("body",self.body)
        dumper.print_member("cond",self.cond)
    
    def accept(self,visitor):
        return visitor.visit(self)