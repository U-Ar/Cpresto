from .ExprNode import ExprNode

class BinaryOpNode(ExprNode):
    def __init__(self,left,op,right,t=None):
        super().__init__()
        self._operator = op
        self._left = left
        self._right = right
        self._type = t

    
    def operator(self):
        return self._operator
    
    def type(self):
        if self._type == None:
            return self._left.type()
        else:
            return self._type
    
    def set_type(self,t):
        if self._type != None:
            raise Exception("BinaryOp.set_type called twice")
        self._type = t
    
    def left(self):
        return self._left
    
    def right(self):
        return self._right
    
    def set_left(self,left):
        self._left = left
    
    def set_right(self,right):
        self._right = right
    
    def location(self):
        return self._left.location()
    
    def _dump(self,dumper):
        dumper.print_member("operator", self._operator)
        dumper.print_member("left", self._left)
        dumper.print_member("right", self._right)

    def accept(visitor):
        return visitor.visit(self)