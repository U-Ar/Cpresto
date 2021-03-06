from .NamedSymbol import NamedSymbol

class SymbolTable:
    DUMMY_SYMBOL_BASE = "L"

    @staticmethod
    def dummy():
        #return SymbolTable.dummy
        return DUMMY_SYMBOL_TABLE
    
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

DUMMY_SYMBOL_TABLE = SymbolTable(SymbolTable.DUMMY_SYMBOL_BASE)