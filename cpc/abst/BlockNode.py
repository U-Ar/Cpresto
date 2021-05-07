import entity
from .StmtNode import StmtNode

class BlockNode(StmtNode):
    def __init__(self,loc,vs,stmts):
        super().__init__(loc)
        self.variables = vs
        self.stmts = stmts
    
    def variables(self):
        return self.variables
    
    def stmts(self):
        return self.stmts
    
    def tail_stmt(self):
        if len(self.stmts) == 0:
            return None
        return self.stmts[-1]
    
    def scope(self):
        return self.scope
    
    def set_scope(self,scope):
        self.scope = scope
    
    def _dump(self,dumper):
        dumper.print_node_list("variables", variables)
        dumper.print_node_list("stmts", stmts)
    
    def accept(self,visitor):
        return visitor.visit(self)

    
