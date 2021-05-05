from .CompileException import CompileException
class FileException(CompileException):
    def __init__(self,msg):
        super().__init__(msg)