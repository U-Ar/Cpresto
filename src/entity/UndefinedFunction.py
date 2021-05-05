from Function import Function

class UndefinedFunction(Function):
    def __init__(self,t,name,params):
        super().__init__(False,t,name)
        self.params = params
    
    def parameters(self):
        return self.params.parameters()
    
    def is_defined(self):
        return False
    
    def _dump(self,dumper):
        dumper.print_member("name",self.name)
        dumper.print_member("is_private",self.is_private)
        dumper.print_member("type_node",self.type_node)
        dumper.print_member("params",self.params)
    
    def accept(self,visitor):
        return visitor.visit(self)