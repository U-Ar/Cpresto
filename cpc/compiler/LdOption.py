from .LdArg import LdArg

class LdOption(LdArg):
    def __init__(self,arg):
        self.arg = arg
    
    def is_source_file(self):
        return False
    
    def to_string(self):
        return arg
