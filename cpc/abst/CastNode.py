from type.Type import Type
from .TypeNode import TypeNode
from .ExprNode import ExprNode

class CastNode(ExprNode):
    def __init__(self,t,expr):
        if isinstance(t,TypeNode):
            self.type_node = t
        else :
            self.type_node = TypeNode(t)
        self.expr = expr
    
    def type(self):
        return self.type_node.type()
    
    def type_node(self):
        return self.type_node
    
    def expr(self):
        return self.expr
    
    def is_lvalue(self):
        return self.expr.is_lvalue()
    
    def is_assignable(self):
        return self.expr.is_assignable()
    
    def is_effective_cast(self):
        return self.type().size() > self.expr.type().size()

    def location(self):
        return self.type_node.location()

    def _dump(self,dumper):
        dumper.print_member("TypeNode", self.type_node)
        dumper.print_member("expr", self.expr)
    
    def accept(self,visitor):
        return visitor.visit(self)
