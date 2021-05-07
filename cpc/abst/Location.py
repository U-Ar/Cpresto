from .CprestoToken import CprestoToken

class Location:
    def __init__(self,sourcename,token,kindname=""):
        self._source_name = sourcename
        if isinstance(token,CprestoToken):
            self._token = token
        else :
            self._token = CprestoToken(token,kindname)
    
    def source_name(self):
        return self._source_name
    
    def token(self):
        return self._token
    
    def lineno(self):
        return self._token.lineno()
    
    def column(self):
        return self._token.column()
    
    def line(self):
        return self._token.included_line()
    
    def numbered_line(self):
        return "line " + self._token.lineno() + ": " + self.line()
    
    def to_string(self):
        return self._source_name + ":" + self._token.lineno()
