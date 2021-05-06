from abc import ABCMeta, abstractmethod
from .ExprNode import ExprNode

class LHSNode(ExprNode):
    def __init__(self):
        super().__init__()
        self.type = None
        self.orig_type = None
    
    def type(self):
        if self.type == None:
            return self.orig_type()
        else:
            return self.type
    
    def set_type(self,t):
        self.type = t
    
    @abstractmethod
    def orig_type(self):
        pass

    def alloc_size(self):
        return self.orig_type().alloc_size()
    
    def is_lvalue(self):
        return True
    
    def is_assignable(self):
        return self.is_loadable()
    
    def is_loadable(self):
        t = self.orig_type()
        return (not t.is_array()) and (not t.is_function())