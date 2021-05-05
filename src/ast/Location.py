from .CflatToken import CflatToken

class Location:
    def __init__(self,sourcename,token):
        self.source_name = sourcename
        if isinstance(token,CflatToken):
            self.token = token
        else :
            self.token = CflatToken(token)
    
    def source_name(self):
        return self.source_name
    
    def token(self):
        return self.token
    
    def lineno(self):
        return self.token.lineno()
    
    def column(self):
        return self.token.column()
    
    def line(self):
        return self.token.included_line()
    
    def numbered_line(self):
        return "line " + self.token.lineno() + ": " + self.line()
    
    def to_string(self):
        return self.source_name + ":" + self.token.lineno()
