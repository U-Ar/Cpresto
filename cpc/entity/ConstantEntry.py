class ConstantEntry:
    def __init__(self,val):
        self.value = val
        self.symbol = None
        self.memref = None
        self.address = None
    
    def value(self):
        return self.value
    
    def set_symbol(self,sym):
        self.symbol = sym
    
    def symbol(self):
        if self.symbol == None:
            raise Exception("must not happen: symbol == None")
        return self.symbol
    
    def set_memref(self,mem):
        self.memref = mem
    
    def memref(self):
        if self.memref == None:
            raise Exception("must not happen: memref == None")
        return self.memref

    def set_address(self,imm):
        self.address = imm
    
    def address(self):
        return self.address