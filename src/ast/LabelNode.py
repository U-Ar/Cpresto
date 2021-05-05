class LabelNode(StmtNode):
    def __init__(self,loc,name,stmt):
        super().__init__(loc)
        self.name = name
        self.stmt = stmt
    
    def name(self):
        return self.name
    
    def stmt(self):
        return self.stmt
    
    def _dump(self,dumper):
        dumper.print_member("name",self.name)
        dumper.print_member("stmt",self.stmt)
    
    def accept(self,visitor):
        return visitor.visit(self)