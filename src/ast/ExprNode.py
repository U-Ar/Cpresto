from ..exception import *
from abc import ABCMeta, abstractmethod

class ExprNode(Node):
    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def type(self):
        pass

    def orig_type(self):
        return self.type()
    
    def alloc_size(self):
        return self.type().alloc_size()
    
    def is_constant(self):
        return False
    
    def is_parameter(self):
        return False
    
    def is_lvalue(self):
        return False
    
    def is_assignable(self):
        return False
    
    def is_loadable(self):
        return False

    def is_callable(self):
        try:
            return self.type().is_callable()
        except SemanticError.SemanticError as err:
            return False
    
    def is_pointer(self):
        try:
            return self.type().is_pointer()
        except SemanticError.SemanticError as err:
            return False
    
    @abstractmethod
    def accept(self,visitor):
        pass