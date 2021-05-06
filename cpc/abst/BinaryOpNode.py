class BinaryOpNode(ExprNode):
    def __init__(self,left,op,right,t=None):
        super().__init__()
        self.operator = op
        self.left = left
        self.right = right
        self.type = t

    
    def operator(self):
        return self.operator
    
    def type(self):
        if self.type == None:
            return self.left.type
        else:
            return self.type
    
    def set_type(self,t):
        if self.type != None:
            raise Exception("BinaryOp.set_type called twice")
        self.type = t
    
    def left(self):
        return self.left
    
    def right(self):
        return self.right
    
    def set_left(self,left):
        self.left = left
    
    def set_right(self,right):
        self.right = right
    
    def location(self):
        return self.left.location()
    
    def _dump(self,dumper):
        dumper.print_member("operator", self.operator)
        dumper.print_member("left", self.left)
        dumper.print_member("right", self.right)

    def accept(visitor):
        return visitor.visit(self)