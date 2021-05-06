from abc import ABCMeta, abstractmethod
class ASTVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self,node):
        pass