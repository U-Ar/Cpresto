from .ExprNode import ExprNode
from exception.SemanticError import SemanticError

class FuncallNode(ExprNode):
    def __init__(self,expr,args):
        self.expr = expr
        self.args = args
    
    def expr(self):
        return self.expr
    
    def type(self):
        try:
            return self.function_type().return_type()
        except Exception as ex:
            raise SemanticError(ex.message)
    
    def function_type(self):
        return self.expr.type().get_pointer_type().base_type().get_function_type()

    def num_args(self):
        return len(self.args)
    
    def args(self):
        return self.args
    
    def replace_args(self,args):
        self.args = args
    
    def location(self):
        return self.expr.location
    
    def _dump(self,dumper):
        dumper.print_member("expr", self.expr)
        dumper.print_node_list("args", self.args)
    
    def accept(self,visitor):
        return visitor.visit(self)