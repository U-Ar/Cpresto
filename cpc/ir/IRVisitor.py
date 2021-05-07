from abc import ABCMeta,abstractmethod
class IRVisitor:
    @abstractmethod
    def visit(self,s):
        pass
