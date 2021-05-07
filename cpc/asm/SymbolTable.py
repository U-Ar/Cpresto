from .NamedSymbol import NamedSymbol

class SymbolTable:
    DUMMY_SYMBOL_BASE = "L"
    dummy = SymbolTable(SymbolTable.DUMMY_SYMBOL_BASE)

    @classmethod
    def dummy():
        return SymbolTable.dummy
    
    def __init__(self,base):
        self.base = base
        self.map = dict()
        self.seq = 0
    
    def new_symbol(self):
        return NamedSymbol(self.new_string())
    
    def symbol_string(self,sym):
        if sym in self.map:
            return map[sym]
        else:
            new_str = self.new_string()
            map[sym] = new_str
            return new_str
    
    def new_string(self):
        self.seq += 1
        return str(self.base + self.seq - 1)