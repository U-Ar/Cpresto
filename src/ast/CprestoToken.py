from ..parser.CprestoParser import CprestoParser
from ..utils.TextUtils import TextUtils

class CprestoToken:
    def __init__(self,token,is_special=None):
        if is_special == None:
            self.is_special = False
        else :
            self.is_special = is_special
        self.token = token
    
    def to_string(self):
        return self.token.text
    
    def is_special(self):
        return self.is_special
    
    def kind_ID(self):
        return self.token.getType()
    
    def kind_name(self):
        voc = CprestoParser.getVocabulary()
        res = voc.getSymbolicName(self.token.getType())
        return res

    def lineno(self):
        return self.token.line
    
    def column(self):
        return self.token.pos

    def image(self):
        return self.token.text

    def dumped_image(self):
        return TextUtils.dump_string(self.token.text)
    
    def ite
