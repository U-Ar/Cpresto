from .Assembly import Assembly

class Instruction(Assembly):
    def __init__(self,a1,a2=None,a3=None,a4=None,a5=False):
        if isinstance(a3,list):
            self.mnemonic = a1
            self.suffix = a2
            self.operands = a3
            self.need_relocation = a4
        else :
            if a4 != None:
                self.mnemonic = a1
                self.suffix = a2
                self.operands = [a3,a4]
                self.need_relocation = a5
            elif a3 != None:
                self.mnemonic = a1
                self.suffix = a2
                self.operands = [a3]
                self.need_relocation = a5
            else :
                self.mnemonic = a1
                self.suffix = ""
                self.operands = []
                self.need_relocation = False

    def build(self, mnemonic,o1,o2=None):
        if o2 == None:
            return Instruction(mnemonic,self.suffix,[o1],self.need_relocation)
        else :
            return Instruction(mnemonic,self.suffix,[o1,o2],self.need_relocation)
    
    def is_instruction(self):
        return True
    
    def mnemonic(self):
        return self.mnemonic
    
    def is_jump_instruction(self):
        return self.mnemonic == "jmp" or self.mnemonic == "jz" or \
            self.mnemonic == "jne" or self.mnemonic == "je"
    
    def num_operands(self):
        return len(self.operands)
    
    def operand1(self):
        return self.operands[0]
    
    def operand2(self):
        return self.operands[1]
    
    def jmp_destination(self):
        ref = self.operands[0]
        return ref.value()
    
    def collect_statistics(self,stats):
        stats.instrunction_used(self.mnemonic)
        for i in range(len(self.operands)):
            self.operands[i].collect_statistics(stats)
    
    def to_source(self,table):
        buf = "\t"
        buf += self.mnemonic + self.suffix
        sep = "\t"
        for i in range(len(self.operands)):
            buf += sep
            sep = ", "
            buf += self.operands[i].to_source(table)
        return buf

    def to_string(self):
        return "#<Insn " + self.mnemonic + ">"

    def dump(self):
        buf = "(Instruction "
        buf += TextUtils.dump_string(self.mnemonic)
        buf += " "
        buf += TextUtils.dump_string(self.suffix)
        for oper in self.operands:
            buf += " " + oper.dump()
        buf += ")"
        return buf
    
        
