from .IRDumpable import IRDumpable

class Case(IRDumpable):
    def __init__(self,value,label):
        self._value = value
        self._label = label
    
    def dump(self, dumper):
        dumper.print_class(self)
        dumper.print_member("value",self._value)
        dumper.print_member("label",self._label)