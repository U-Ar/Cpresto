from asm.Assembly import Assembly

class Label(Assembly):
    def __init__(self,sym=None):
        if sym == None:
            self.symbol = UnnamedSymbol()
        else:
            self.symbol = sym
        
    def symbol(self):
        return self.symbol
    
    def is_labels(self):
        return True
    
    def to_source(self,table):
        return self.symbol.to_source(table) + ":"
    
    def dump(self):
        return "(Label " + self.symbol.dump() + ")" 