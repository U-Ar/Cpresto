from abc import ABCMeta,abstractmethod

class PeepholeOptimizer:
    def __init__(self):
        self.filter_set = dict()
    
    def add(self,fil):
        heads = fil.pattern_heads()
        for i in range(len(heads)):
            head = heads[i]
            if head not in self.filter_set:
                lis = []
                lis.append(fil)
                self.filter_set[head] = lis
            else :
                self.filter_set[head].append(fil)
    
    def optimize(self,asms):
        res = []
        for idx in range(len(asms)):
            asm = asms[idx]
            if asm.is_instruction():
                matched = self.match_filter(asms,idx)
                if matched != None:
                    matched.optimize(asms,idx,res)
                    continue
            res.append(asm)
        return result
    
    def match_filter(self,asms,idx):
        insn = asms[idx]
        if insn.mnemonic() not in self.filter_set:
            return None
        filters = self.filter_set[insn.mnemonic()]
        if len(filters) == 0:
            return None
        for f in filters:
            if f.match(asms,idx):
                return f
        return None

    @staticmethod
    def default_set():
        s = PeepholeOptimizer()
        s.load_default_filters()
        return s
    
    def load_default_filters(self):
        s = self

        # mov 
        s.add(SingleInsnFilter(InsnPattern("mov",self.imm(0),self.reg()),
            lambda insn: insn.build("xor",insn.operand2(),insn.operand2())))
        
        #add
        s.add(SingleInsnFilter(InsnPattern("add",self.imm(-1),self.reg()),
            lambda insn: insn.build("dec",insn.operand2())))
        s.add(SingleInsnFilter(InsnPattern("add",self.imm(0),self.reg()),
            None))
        s.add(SingleInsnFilter(InsnPattern("add",self.imm(1),self.reg()),
            lambda insn: insn.build("inc",insn.operand2())))
        
        #sub
        s.add(SingleInsnFilter(InsnPattern("sub",self.imm(-1),self.reg()),
            lambda insn: insn.build("inc",insn.operand2())))
        s.add(SingleInsnFilter(InsnPattern("sub",self.imm(0),self.reg()),
            None))
        s.add(SingleInsnFilter(InsnPattern("sub",self.imm(1),self.reg()),
            lambda insn: insn.build("dec",insn.operand2())))
        
        #imul 
        s.add(SingleInsnFilter(InsnPattern("imul",self.imm(0),self.reg()),
            lambda insn: insn.build("xor",insn.operand2(),insn.operand2())))
        s.add(SingleInsnFilter(InsnPattern("imul",self.imm(1),self.reg()),
            None))
        s.add(SingleInsnFilter(InsnPattern("sub",self.imm(2),self.reg()),
            lambda insn: insn.build("sal",self.imm(1),insn.operand2())))
        s.add(SingleInsnFilter(InsnPattern("sub",self.imm(4),self.reg()),
            lambda insn: insn.build("sal",self.imm(2),insn.operand2())))
        s.add(SingleInsnFilter(InsnPattern("sub",self.imm(8),self.reg()),
            lambda insn: insn.build("sal",self.imm(3),insn.operand2())))
        s.add(SingleInsnFilter(InsnPattern("sub",self.imm(16),self.reg()),
            lambda insn: insn.build("sal",self.imm(4),insn.operand2())))
        
        s.add(JumpEliminationFilter())

        
    
    def imm(self,n):
        return ImmediateValue(n)
    def reg(self):
        return AnyRegisterPattern()

    class Filter(metaclass=ABCMeta):
        @abstractmethod
        def pattern_heads(self):
            pass
        @abstractmethod
        def match(self,asms):
            pass
        @abstractmethod
        def optimize(self,srcs,i,dest):
            pass
    
    class SingleInsnFilter(Filter):
        def __init__(self,pat,tr):
            self.pattern = pattern
            self.transform = transform
        
        def pattern_heads(self):
            return [self.pattern.name]
        
        def match(self,asms,i):
            return self.pattern.match(asms,i)
        
        def optimize(self,srcs,i,dest):
            if self.transform = None:
                pass
            else :
                dest.append(self.tranform(srcs[i]))
    
    class InsnPattern:
        def __init__(self,name,pat1,pat2):
            self.name = name
            self.pattern1 = pat1
            self.pattern2 = pat2
        
        def match(self,insn):
            return self.name == insn.mnemonic() and \
                (self.pattern1 == None or self.pattern1.match(insn.operand1())) and \
                    (self.pattern2 == None or self.pattern2.match(insn.operand2()))
        
    class AnyRegisterPattern(OperandPattern):
        def match(self,operand):
            return operand.is_register()
    
    #
    # jump elimination
    #

    class JumpEliminationFilter(Filter):
        def __init__(self):
            pass
        
        def jmp_insns(self):
            return ["jmp","jz","jne","je","jne"]
        
        def pattern_heads(self):
            return self.jmp_insns()
        
        def optimize(self,srcs,i,dest):
            pass # remove jump
    
        def match(self,asms,i):
            insn = asms[i]
            return self.does_label_follows(asms,i,insn.jmp_destination())
    
        def does_label_follows(self,asms,i,jmp_dest):
            for j in range(i,len(asms)-1):
                asm = asms[j+1]
                if asm.is_label():
                    if asm.symbol().equals(jmp_dest):
                        return True
                    else :
                        continue
                elif asm.is_comment():
                    continue
                else :
                    return False
            return False        

    

