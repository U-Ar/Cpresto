from .SemanticError import SemanticError

class JumpError(SemanticError):
    def __init__(self,msg):
        super().__init__(msg)