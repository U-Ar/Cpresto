from abc import ABCMeta,abstractmethod
class IRVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self,s):
        pass
