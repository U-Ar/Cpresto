class SwitchNode(StmtNode):
    def __init__(self,loc,cond,cases):
        super().__init__(loc)
        self.cond = cond
        self.cases = cases
    
    def cond(self):
        return self.cond
    
    def cases(self):
        return self.cases
    
    def _dump(self,dumper):
        dumper.print_member("cond",cond)
        dumper.print_node_list("cases",cases)
    
    def accept(self,visitor):
        return visitor.visit(self)