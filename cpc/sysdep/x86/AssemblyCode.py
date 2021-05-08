import sys
import sysdep.AssemblyCode
import asm

class AssemblyCode(sysdep.AssemblyCode):
    def __init__(self,natural_type,stack_word_size,
                 label_symbols, verbose):
        self.natural_type = natural_type
        self.stack_word_size = stack_word_size
        self.label_symbols = label_symbols
        self.verbose = verbose

        self.virtual_stack = VirtualStack(self.natural_type)
        self.assemblies = []
        self.comment_indent_level = 0
        self.stats = None

    def assemblies(self):
        return self.assemblies

    def add_all(self,assem):
        self.assemblies += assem
    
    def to_source(self):
        buf = ""
        for asm in assemblies:
            buf += asm.to_source(self.label_symbols)
            buf += "\n"
        return buf.to_string()
    
    def dump(self,s=None):
        if s == None:
            dump(sys.stdout)
        else :
            for asm in self.assemblies:
                s.write(asm.dump() + "\n")
    
    def apply(self,opt):
        self.assemblies = opt.optimize(self.assemblies)
    
    def statistics(self):
        if self.stats == None:
            self.stats = Statistics.collect(self.assemblies)
        return self.stats
    
    def does_uses(self,reg):
        return self.statistics().does_register_used(reg)
    
    def comment(self,s):
        self.assemblies.append(Comment(s,self.comment_indent_level))
    
    def indent_comment(self):
        self.comment_indent_level += 1
    
    def unindent_comment(self):
        self.comment_indent_level -= 1
    
    def label(self,sym):
        if isinstance(sym,Symbol):
            self.assemblies.append(Label(sym))
        else :
            self.assemblies.append()
    
    def reduce_labels(self):
        stats = self.statistics()
        res = []
        for asm in self.assemblies:
            if asm.is_label() and not stats.does_symbol_used(asm):
                pass
            else :
                res.append(asm)
        self.assemblies = res
    
    def directive(self,di):
        self.assemblies.append(Directive(di))

    def insn(self,a1=None,a2=None,a3=None,a4=None):
        if a4 != None:
            if isinstance(a1,str):
                self.assemblies.append(Instruction(a1,a2,a3,a4))
            else :
                self.assemblies.append(Instruction(a1,self.type_suffix(a2),a3,a4))
        elif a3 != None:
            if isinstance(a1,str):
                self.assemblies.append(Instruction(a1,a2,a3))
            else :
                self.assemblies.append(Instruction(a2,self.type_suffix(a1),a3))
        elif a2 != None:
            self.assemblies.append(Instruction(a1,"",a2))
        else :
            self.assemblies.append(Instruction(a1))
    
    def type_suffix(self,t1,t2=None):
        if t2 == None:
            if t1 == Type.INT8:
                return "b"
            elif t1 == Type.INT16:
                return "w"
            elif t1 == Type.INT32:
                return "l"
            elif t1 == Type.INT64:
                return "q"
            else :
                raise Exception("unknown register type: " + str(t1.size()))
        else :
            return self.type_suffix(t1) + self.type_suffix(t2)

    #
    # directives
    #

    def _file(self,name):
        self.directive(".file\t"+TextUtils.dump_string(name))
    def _text(self):
        self.directive("\t.text")
    def _data(self):
        self.directive("\t.data")
    def _section(self,name,flags=None,t=None,group=None,linkage=None):
        if flags == None:
            self.directive("\t.section\t"+name)
        else :
            self.directive("\t.section\t"+name+","+flags+","+t+","+group+","+linkage)
    def _globl(self,sym):
        self.directive(".globl " + sym.name())
    def _local(self,sym):
        self.directive(".local " + sym.name())
    def _hidden(self,sym):
        self.directive("\t.hidden\t" + sym.name())
    def _comm(self,sym,size,alignment):
        self.directive("\t.comm\t" + sym.name()+","+str(size)+str(alignment))
    def _align(self,n):
        self.directive("\t.align\t" + str(n))
    def _type(self,sym,t):
        self.directive("\t.type\t"+sym.name()+","+t)
    def _size(self,sym,size):
        if isinstance(size,str):
            self.directive("\t.size\t" + sym.name()+","+size)
        else :
            self.directive("\t.size\t" + sym.name()+","+str(size))
    def _byte(self,val):
        if isinstance(val,int):
            self.directive(".byte\t" + IntegerLiteral(val).to_source())
        else :
            self.directive(".byte\t" + val.to_source())
    def _value(self,val):
        if isinstance(val,int):
            self.directive(".value\t"+IntegerLiteral(val).to_source())
        else :
            self.directive(".value\t" + val.to_source())
    def _long(self,val):
        if isinstance(val,int):
            self.directive(".long\t"+IntegerLiteral(val).to_source())
        else :
            self.directive(".long\t" + val.to_source())
    def _quad(self,val):
        if isinstance(val,int):
            self.directive(".quad\t"+IntegerLiteral(val).to_source())
        else :
            self.directive(".quad\t" + val.to_source())
    def _string(self,s):
        self.directive("\t.string\t"+TextUtils.dump_string(s))

    #
    # Virtual Stack
    #

    class VirtualStack:
        def __init__(self,natural_type):
            self.offset = None
            self.max = None
            self.memrefs = []
            self.natural_type = natural_type
            self.reset()
        
        def reset(self):
            self.offset = 0
            self.max = 0
            self.memrefs.clear()
        
        def max_size(self):
            return self.max

        def extend(self,l):
            self.offset += l
            self.max = max(self.offset,self.max)
        
        def rewind(self,l):
            self.offset -= l
        
        def top(self):
            mem = self.relocatable_mem(-self.offset,self.bp())
            self.memrefs.append(mem)
            return mem
        
        def relocatable_mem(self,offset,base):
            return IndirectMemoryReference.relocatable(offset,base)
        
        def bp(self):
            return Register(RegisterClass.BP,self.natural_type)
        
        def fix_offset(self,dif):
            for mem in self.memrefs:
                mem.fix_offset(dif)
    
    # Virtual Stack end


    def virtual_push(self,reg):
        if self.verbose:
            self.comment("push " + reg.base_name() + " -> " + self.virtual_stack.top())
        self.virtual_stack.extend(self.stack_word_size)
        self.mov(reg,self.virtual_stack.top())
    
    def virtual_pop(self,reg):
        if self.verbose:
            self.comment("pop " + reg.base_name() + " <- " + self.virtual_stack.top())
        self.mov(self.virtual_stack.top(),reg)
        self.virtual_stack.rewind(self.stack_word_size)


    #
    # Instructions
    #

    def jmp(self,label):
        self.insn("jmp",DirectMemoryReference(label.symbol()))
    def jnz(self,label):
        self.insn("jnz",DirectMemoryReference(label.symbol()))
    def je(self,label):
        self.insn("je",DirectMemoryReference(label.symbol())) 
    def cmp(self,a,b):
        self.insn(b.type(),"cmp",a,b)
    def sete(self,reg):
        self.insn("sete",reg)
    def setne(self,reg):
        self.insn("setne",reg)
    def seta(self,reg):
        self.insn("seta",reg)
    def setae(self,reg):
        self.insn("setae",reg)
    def setb(self,reg):
        self.insn("setb",reg)
    def setbe(self,reg):
        self.insn("setbe",reg)
    def setg(self,reg):
        self.insn("setg",reg)
    def setge(self,reg):
        self.insn("setge",reg)
    def setl(self,reg):
        self.insn("setl",reg)
    def setle(self,reg):
        self.insn("setle",reg)
    def test(self,a,b):
        self.insn(b.type(),"test",a,b)
    def push(self,reg):
        self.insn("push",self.type_suffix(self.natural_type),reg)
    def pop(self,reg):
        self.insn("pop",self.type_suffix(self.natural_type),reg)
    def call(self,sym):
        self.insn("call",DirectMemoryReference(sym))
    def call_absolute(self,reg):
        self.insn("call",AbsoluteAddress(reg))
    def ret(self):
        self.insn("ret")
    def mov(self,src,dest):
        if isinstance(src,Operand): # load
            self.insn(dest.type(),"mov",src,dest)
        elif isinstance(dest,Operand): # store
            self.insn(src.type(),"mov",src,dest)
        else :
            self.insn(self.natural_type,"mov",src,dest)
    # for stack access
    def relocatable_mov(self,src,dest):
        self.assemblies.append(Instruction("mov",self.type_suffix(self.natural_type),src,dest,True))
    
    def movsx(self,src,dest):
        self.insn("movs",self.type_suffix(src.type(),dest.type()),src,dest)
    def movzx(self,src,dest):
        self.insn("movz",self.type_suffix(src.type(),dest.type()),src,dest)
    def movzb(self,src,dest):
        self.insn("movz","b"+self.type_suffix(dest.type()),src,dest)
    def lea(self,src,dest):
        self.insn(self.natural_type,"lea",srd,dest)
    def neg(self,reg):
        self.insn(reg.type(),"neg",reg)
    def add(self,dif,base):
        self.insn(base.type(),"add",dif,base)
    def sub(self,dif,base):
        self.insn(base.type(),"sub",dif,base)
    def imul(self,m,base):
        self.insn(base.type(),"imul",m,base)
    def cltd(self):
        self.insn("cltd")
    def div(self,base):
        self.insn(base.type(),"div",base)
    def idiv(self,base):
        self.insn(base.type(),"idiv",base)
    def not_(self,reg):
        self.insn(reg.type(),"not",reg)
    def and_(self,bits,base):
        self.insn(base.type(),"and",bits,base)
    def or_(self,bits,base):
        self.insn(base.type(),"or",bits,base)
    def xor(self,bits,base):
        self.insn(base.type(),"xor",bits,base)
    def sar(self,bits,base):
        self.insn(base.type(),"sar",bits,base)
    def sal(self,bits,base):
        self.insn(base.type(),"sal",bits,base)
    def shr(self,bits,base):
        self.insn(base.type(),"shr",bits,base)
    
        
    


    
