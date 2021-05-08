from .Expr import Expr
from entity.Function import Function

class Call(Expr):
    def __init__(self,t,expr,args):
        super().__init__(t)
        self._expr = expr
        self._args = args

    def expr(self):
        return self._expr

    def args(self):
        return self._args
    
    def num_args(self):
        return len(self._args)
    
    def is_static_call(self):
        return isinstance(self._expr.get_entity_force(),Function)

    def function(self):
        ent = self._expr.get_entity_force()
        if ent == None:
            raise Exception("not a static funcall")
        return ent
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("expr",self._expr)
        dumper.print_members("args",self._args)