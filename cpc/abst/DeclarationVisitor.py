from abc import ABCMeta,abstractmethod

class DeclarationVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self,node):
        pass