from .CompileException import CompileException

class SemanticException(CompileException):
    def __init__(self,msg):
        super().__init__(msg)