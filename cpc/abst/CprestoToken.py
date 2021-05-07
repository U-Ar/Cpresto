from utils.TextUtils import TextUtils

class CprestoToken:
    def __init__(self,token,kindname,is_special=None):
        if is_special == None:
            self.is_special = False
        else :
            self.is_special = is_special
        self.token = token
        self.kind_name = kindname
    
    def to_string(self):
        return self.token.text
    
    def is_special(self):
        return self.is_special
    
    def kind_ID(self):
        return self.token.getType()
    
    def kind_name(self):
        return self.kind_name

    def lineno(self):
        return self.token.line
    
    def column(self):
        return self.token.pos

    def image(self):
        return self.token.text

    def dumped_image(self):
        return TextUtils.dump_string(self.token.text)
    
    #def iterator

    def tokens_without_first_specials(self):
        return self.build_token_list(self.token,True)
    
    def build_token_list(self,first,reject):
        pass
        #res = []
        #while 
