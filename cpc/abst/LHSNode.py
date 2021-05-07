from abc import ABCMeta, abstractmethod
from .ExprNode import ExprNode

class LHSNode(ExprNode):
    def __init__(self):
        super().__init__()
        self._type = None
        self._orig_type = None
    
    def type(self):
        if self._type == None:
            return self.orig_type()
        else:
            return self._type
    
    def set_type(self,t):
        self._type = t
    
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