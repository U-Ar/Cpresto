from .BaseSymbol import BaseSymbol

class UnnamedSymbol(BaseSymbol):
    def __init__(self):
        super().__init__()

    def name(self):
        raise Exception("unnamed symbol")

    def to_source(self,table=None):
        if table == None:
            raise Exception("UnnamedSymbol.to_source() called")
        else :
            return table.symbol_string(self)
    
    def to_string(self):
        return super().to_string()

    def compare_to(self,lit):
        return -(lit.compare_to(self))
    
    def cmp(self,i):
        if isinstance(i,UnnamedSymbol):
            return self.to_string().compare_to(i.to_string())
        else :
            return 1
    
    def dump(self):
        return "(UnnamedSymbol @" +self.to_string()+ ")"