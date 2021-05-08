from .Expr import Expr
from asm.ImmediateValue import ImmediateValue

class Int(Expr):
    def __init__(self,t,value):
        super().__init__(t)
        self._value = value

    def value(self):
        return self._value
    
    def is_constant(self):
        return True
    
    def asm_value(self):
        return ImmediateValue(IntegerLiteral(self._value))
    
    def memref(self):
        raise Exception("must not happen: IntValue.memref")
    
    def accept(self,visitor):
        return visitor.visit(self)
    
    def _dump(self,dumper):
        dumper.print_member("value",self._value)