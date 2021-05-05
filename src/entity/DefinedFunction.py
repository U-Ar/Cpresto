from Function import Function

class DefinedFunction(Function):
    def __init__(self, priv, t, name, params, body):
        super().__init__(priv, t, name)
        self.params = params
        self.body = body
        self.ir = []
        self.scope = None
    
    def is_defined(self):
        return True
    
    def parameters(self):
        return self.params.parameters()
    
    def body(self):
        return self.body
    
    def ir(self):
        return self.ir
    
    def set_IR(self,ir):
        self.ir = ir
    
    def set_scope(self,scope):
        self.scope = scope
    
    def lvar_scope(self):
        return self.body().scope()
    
    # Returns function local variables.
    # Does NOT include paramters.
    # Does NOT include static local variables.
    def local_variables(self):
        return self.scope.all_local_variables()
    
    def _dump(self,dumper):
        dumper.print_member("name", self.name)
        dumper.print_member("is_private", self.is_private)
        dumper.print_member("params", self.params)
        dumper.print_member("body", self.body)
    
    def accept(self,visitor):
        return visitor.visit(self)
    
