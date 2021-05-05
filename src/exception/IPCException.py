from .CompileException import CompileException

class IPCException(CompileException):
    def __init__(self,msg):
        super().__init__(msg)