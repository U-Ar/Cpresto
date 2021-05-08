from .Assembly import Assembly
from utils.TextUtils import TextUtils

class Directive(Assembly):
    def __init__(self,content):
        self._content = content

    def is_directive(self):
        return True
    
    def to_source(self,table):
        return self._content

    def dump(self):
        return "(Directive " + TextUtils.dump_string(self._content.lstrip().rstrip()) + ")"

