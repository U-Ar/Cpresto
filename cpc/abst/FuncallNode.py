from .ExprNode import ExprNode
from exception.SemanticError import SemanticError

class FuncallNode(ExprNode):
    def __init__(self,expr,args):
        self._expr = expr
        self._args = args
    
    def expr(self):
        return self._expr
    
    def type(self):
        try:
            return self.function_type().return_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def function_type(self):
        return self._expr.type().get_pointer_type().base_type().get_function_type()

    def num_args(self):
        return len(self._args)
    
    def args(self):
        return self._args
    
    def replace_args(self,args):
        self._args = args
    
    def location(self):
        return self._expr.location()
    
    def _dump(self,dumper):
        dumper.print_member("expr", self._expr)
        dumper.print_node_list("args", self._args)
    
    def accept(self,visitor):
        return visitor.visit(self)