from .CompileException import CompileException

class SyntaxException(CompileException):
    def __init__(self,msg):
        super().__init__(msg)