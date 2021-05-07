from .Assembly import Assembly
from utils.TextUtils import TextUtils

class Comment(Assembly):
    def __init__(self,string,indent_level=0):
        self.indent_level = indent_level
        self.string = string
    
    def is_comment(self):
        return True
    
    def to_source(self, table):
        return "\t" + self.indent() + "# " + self.string
    
    def indent(self):
        buf = ""
        for i in range(self.indent_level):
            buf += "  "
        return buf
    
    def dump(self):
        return "(Comment " + TextUtils.dump_string(self.string) + ")"