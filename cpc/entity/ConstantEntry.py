class ConstantEntry:
    def __init__(self,val):
        self._value = val
        self._symbol = None
        self._memref = None
        self._address = None
    
    def value(self):
        return self._value
    
    def set_symbol(self,sym):
        self._symbol = sym
    
    def symbol(self):
        if self._symbol == None:
            raise Exception("must not happen: symbol == None")
        return self._symbol
    
    def set_memref(self,mem):
        self._memref = mem
    
    def memref(self):
        if self._memref == None:
            raise Exception("must not happen: memref == None")
        return self._memref

    def set_address(self,imm):
        self._address = imm
    
    def address(self):
        return self._address