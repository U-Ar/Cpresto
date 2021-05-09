from functools import cmp_to_key

import sysdep.CodeGenerator
import ir
import entity
import asm
from abst.Location import Location
from .ELFConstants import ELFConstants
import utils


class CodeGenerator(sysdep.CodeGenerator,IRVisitor,ELFConstants):

    def __init__(self,options,ntype,eh):
        self.options = options
        self.ntype = ntype
        self.eh = eh

        self.as_ = None
        self.epilogue = None
        self.callee_save_registers_cache = None
    
    def generate(self,ir):
        self.locate_symbols(ir)
        return self.generate_assembly_code(ir)
    
    LABEL_SYMBOL_BASE = ".L"
    CONST_SYMBOL_BASE = ".LC"
    STACK_WORD_SIZE = 4
    GOT = NamedSymbol("_GLOVAL_OFFSET_TABLE_")
    CALLEE_SAVE_REGISTERS = [RegisterClass.BX, RegisterClass.BP,
        RegisterClass.SI, RegisterClass.DI]
    PARAM_START_WORD = 2

    def locate_symbols(self,ir):
        const_symbols = SymbolTable(CodeGenerator.CONST_SYMBOL_BASE)
        for ent in ir.constant_table().entries():
            self.locate_string_literal(ent,const_symbols)
        for var in ir.all_global_variables():
            self.locate_global_variable(var)
        for func in ir.all_functions():
            self.locate_function(func)
    
    def locate_string_literal(self,ent,syms):
        ent.set_symbol(syms.new_symbol())
        if self.options.is_position_independent():
            offset = self.local_GOT_symbol(ent.symbol())
            ent.set_memref(self.mem(offset,self.GOT_base_reg()))
        else :
            ent.set_memref(self.mem(ent.symbol()))
            ent.set_address(self.imm(ent.symbol()))
    
    def locate_global_variable(self,ent):
        sym = self.symbol(ent.symbol_string(),ent.is_private())
        if self.options.is_position_independent():
            if ent.is_private() or self.optimize_gvar_access(ent):
                ent.set_memref(self.mem(self.local_GOT_symbol(sym),self.GOT_base_reg()))
            else :
                ent.set_address(self.mem(self.global_GOT_symbol(sym),self.GOT_base_reg()))
        else :
            ent.set_memref(self.mem(sym))
            ent.set_address(self.imm(sym))
    
    def locate_function(self,func):
        func.set_calling_symbol(self.calling_symbol(func))
        self.locate_global_variable(func)
    
    def symbol(self,sym,is_private):
        return self.private_symbol(sym) if is_private else self.global_symbol(sym)
    
    def global_symbol(self,sym):
        return NamedSymbol(sym)
    
    def private_symbol(self,sym):
        return NamedSymbol(sym)
    
    def calling_symbol(self,func):
        if func.is_private():
            return self.private_symbol(func.symbol_string())
        else :
            sym = self.global_symbol(func.symbol_string())
            return self.PLTSymbol(sym) if self.should_use_PLT(func) else sym
    
    def should_use_PLT(self,ent):
        return self.options.is_position_independent() and not self.optimize_gvar_access(ent)
    
    def optimize_gvar_access(self,ent):
        return self.options.is_PIE_required() and ent.is_defined()

    ## generate assembly code
    def generate_assembly_code(self,ir):
        f = self.new_assembly_code()
        f._file(ir.file_name())
        if ir.is_global_variable_defined():
            self.generate_data_section(f,ir.defined_global_variables())
        if ir.is_string_literal_defined():
            self.generate_read_only_data_section(f,ir.constant_table())
        if ir.is_function_defined():
            self.generate_text_section(f,ir.defined_functions())
        if ir.is_common_symbol_defined():
            self.generate_common_symbols(f,ir.defined_common_symbols())
        if self.options.is_position_independent():
            self.PICThunk(f,self.GOT_base_reg())
        return f

    def new_assembly_code(self):
        return AssemblyCode(self.ntype,CodeGenerator.STACK_WORD_SIZE,
                SymbolTable(CodeGenerator.LABEL_SYMBOL_BASE),
                self.options.is_verbose_asm())
    
    def generate_data_section(self,f,gvars):
        f._data()
        for var in gvars:
            sym = self.global_symbol(var.symbol_string())
            if not var.is_private():
                f._globl(sym)
            f._align(var.alignment())
            f._type(sym,"@object")
            f._size(sym,var.alloc_size())
            f.label(sym)
            self.generate_immediate(f,var.type().alloc_size(),var.ir())
    
    def generate_immediate(self,f,size,node):
        if isinstance(node,Int):
            expr = node
            if f._byte(expr.value()) == 1 or f._value(expr.value()) == 2 or \
                f._long(expr.value()) == 4 or f._quad(expr.value()) == 8:
                break
            else :
                raise Exception("entry size must be 1,2,4,8")
        elif isinstance(node,Str):
            expr = node
            if f._long(expr.symbol()) == 4 or f._quad(expr.symbol()) == 8:
                break
            else :
                raise Exception("pointer size must be 4,8")
        else :
            raise Exception("unknown literal node type "+str(type(node)))

    
    def generate_read_only_data_section(self,f,constants):
        f._section(".rodata")
        for ent in constants:
            f.label(ent.symbol())
            f._string(ent.value())
    
    def generate_text_section(self,f,functions):
        f._text()
        for func in functions:
            sym = self.global_symbol(func.name())
            if not func.is_private():
                f._globl(sym)
            f._type(sym,"@function")
            f.label(sym)
            self.compile_function_body(f,func)
            f._size(sym,".-"+sym.to_source())
    
    def generate_common_symbols(self,f,variables):
        for var in variables:
            sym = self.global_symbol(var.symbol_string())
            if var.is_private():
                f._local(sym)
            f._comm(sym,var.alloc_size(),var.alignment())
    
    def load_GOT_base_address(self,f,reg):
        f.call(self.PICThunkSymbol(reg))
        f.add(self.imm(CodeGenerator.GOT),reg)
    
    def GOT_base_reg(self):
        return self.bx()
    
    def global_GOT_symbol(self,base):
        return SuffixedSymbol(base,"@GOT")

    def local_GOT_symbol(self,base):
        return SuffixedSymbol(base,"@GOTOFF")
    
    def PLT_symbol(self,base):
        return SuffixedSymbol(base,"@PLT")
    
    def PIC_thunk_symbol(self,reg):
        return NamedSymbol("__i686.get_pc_thunk."+reg.base_name())
    
    PIC_thunk_section_flags = ELFConstants.section_flag_allocatable + \
                                ELFConstants.section_flag_executable + \
                                    ELFConstants.section_flag_sectiongroup
    # Output PIC thunk.
    # ELF section declaration format is:
    #
    #     .section NAME, FLAGS, TYPE, flag_arguments
    #
    # FLAGS, TYPE, flag_arguments are optional.
    # For "M" flag (a member of a section group),
    # following format is used:
    #
    #     .section NAME, "...M", TYPE, section_group_name, linkage
    #

    def PIC_thunk(self,f,reg):
        sym = self.PIC_thunk_symbol(reg)
        f._section(".text."+sym.to_source(),"\""+CodeGenerator.PIC_thunk_section_flags +\
            "\"", ELFConstants.section_type_bits,
             sym.to_source(),
             ELFConstants.linkage_linkonce)
        f._globl(sym)
        f._hidden(sym)
        f._type(sym,ELFConstants.symbol_type_function)
        f.label(sym)
        f.mov(self.mem(self.sp()),reg)
        f.ret()


    # Standard IA-32 stack frame layout
    #
    # ======================= esp #3 (stack top just before function call)
    # next arg 1
    # ---------------------
    # next arg 2
    # ---------------------
    # next arg 3
    # ---------------------   esp #2 (stack top after alloca call)
    # alloca area
    # ---------------------   esp #1 (stack top just after prelude)
    # temporary
    # variables...
    # ---------------------   -16(%ebp)
    # lvar 3
    # ---------------------   -12(%ebp)
    # lvar 2
    # ---------------------   -8(%ebp)
    # lvar 1
    # ---------------------   -4(%ebp)
    # callee-saved register
    # ======================= 0(%ebp)
    # saved ebp
    # ---------------------   4(%ebp)
    # return address
    # ---------------------   8(%ebp)
    # arg 1
    # ---------------------   12(%ebp)
    # arg 2
    # ---------------------   16(%ebp)
    # arg 3
    # ...
    # ...
    # ======================= stack bottom


    def align_stack(self,size):
        return AsmUtils.align(size, CodeGenerator.STACK_WORD_SIZE)
    
    def stack_size_from_word_num(self,num):
        return num * CodeGenerator.STACK_WORD_SIZE
    
    class StackFrameInfo:
        def __init__(self):
            self.save_regs = []
            self.lvar_size = 0
            self.temp_size = 0
        def save_regs_size(self):
            return len(self.save_regs) * CodeGenerator.STACK_WORD_SIZE
        def lvar_offset(self):
            return self.save_regs_size()
        def temp_offset(self):
            return self.save_regs_size() + self.lvar_size
        def frame_size(self):
            return self.save_regs_size() + self.lvar_size + self.temp_size
    
    def compile_function_body(self,f,func):
        frame = StackFrameInfo()
        self.locate_parameters(func.parameters())
        frame.lvar_size = self.locate_local_variables(func.lvar_scope())

        body = self.optimize(self.compile_stmts(func))
        frame.save_regs = self.used_callee_save_registers(body)
        frame.temp_size = body.virtual_stack.max_size()

        self.fix_local_variable_offsets(func.lvar_scope(),frame.lvar_offset())
        self.fix_temp_variable_offsets(body,frame.temp_offset())
    
        if self.options.is_verbose_asm():
            self.print_stack_frame_layout(f,frame,func.local_variables())
        
        self.generate_function_body(f,body,frame)

    
    def optimize(self,body):
        if self.options.optimize_level() < 1:
            return body
        body.apply(PeepholeOptimizer.default_set())
        body.reduce_labels()
        return body
    
    def print_stack_frame_layout(self,f,frame,lvars):
        vs = []
        for var in lvars:
            vs.append(MemInfo(var.memref(),var.name()))
        vs.append(MemInfo(self.mem(0,self.bp()),"return address"))
        vs.append(MemInfo(self.mem(4,self.bp()),"saved %%ebp"))
        if frame.save_regs_size() > 0:
            vs.append(MemInfo(self.mem(-frame.save_regs_size(),self.bp()),
                "saved callee-saved registers (" + str(frame.save_regs_size())+" bytes)"))
        if frame.temp_size > 0:
            vs.append(MemInfo(self.mem(-frame.frame_size(),self.bp()),
                "tmp variables (" + frame.temp_size + " bytes)"))
        
        vs.sort(key=cmp_to_key(lambda x, y: x.mem.compare_to(y.mem)))

        f.comment("---- Stack Frame Layout --------")
        for info in vs:
            f.comment(info.mem.to_string()+": "+info.name)
        f.comment("--------------------------------")
    
    class MemInfo:
        def __init__(self,mem,name):
            self.mem = mem
            self.name = name
    

    def compile_stmts(self,func):
        self.as_ = self.new_assembly_code()
        self.epilogue = Label()
        for s in func.ir():
            self.compile_stmt(s)
        self.as_.label(epilogue)
        return self.as_
    
    def used_callee_save_registers(self,body):
        res = []
        for reg in self.callee_save_registers():
            if body.does_used(reg):
                res.append(reg)
        res.pop(self.bp())
        return res

    def callee_save_registers(self):
        if self.callee_save_registers_cache = None:
            regs = []
            for c in CodeGenerator.CALLEE_SAVE_REGISTERS:
                regs.append(Register(c,self.ntype))
            self.callee_save_registers_cache = regs
        return self.callee_save_registers_cache
    
    def generate_function_body(self,f,body,frame):
        f.virtual_stack.reset()
        self.prologue(f,frame.save_regs,frame.frame_size())
        if self.options.is_position_independent() and body.does_uses(self.GOT_base_reg()):
            self.load_GOT_base_address(f,self.GOT_base_reg())
        f.add_all(body.assemblies())
        self.epilogue(f,frame.save_regs)
        f.virtual_stack.fix_offset(0)

    def prologue(self,f,save_regs,frame_size):
        f.push(self.bp())
        f.mov(self.sp(),self.bp())
        for reg in save_regs:
            f.virtual_push(reg)
        self.extend_stack(f,frame_size)
    
    def epilogue(self,f,saved_regs):
        for reg in reversed(saved_regs):
            f.virtual_pop(reg)
        f.mov(self.bp(),self.sp())
        f.pop(self.bp())
        f.ret()
    
    def locate_parameters(self,params):
        num = CodeGenerator.PARAM_START_WORD
        for var in params:
            var.set_memref(self.mem(self.stack_size_from_word_num(num),self.bp()))
            num += 1
    
    def locate_local_variables(self,scope,pstacklen=0):
        l = pstacklen
        for var in scope.local_variables():
            l = self.align_stack(l+var.alloc_size())
            var.set_memref(self.relocatable_mem(-l,self.bp()))
        maxl = l
        for s in scope.children():
            childl = self.locate_local_variables(s,l)
            maxl = max(maxl,childl)
        return maxl
    
    def relocatable_mem(self,offset,base):
        return IndirectMemoryReference.relocatable(offset,base)
    
    def fix_local_variable_offsets(self,scope,l):
        for var in scope.all_local_variables():
            var.memref().fix_offset(-l)
    
    def fix_temp_variable_offsets(self,asm,l):
        asm.virtual_stack.fix_offset(-l)
    
    def extend_stack(self,f,l):
        if l > 0:
            f.sub(self.imm(l),self.sp())
    
    def rewind_stack(self,f,l):
        if l > 0:
            f.add(self.imm(l),self.sp())
    
    #
    # Visit for IR
    #
    def visit(self,node): 




    
    #
    # Utilities
    #
    
    def load_constant(self,node,reg):
        if node.asm_value() != None:
            self.as_.mov(node.asm_value(),reg)
        elif node.memref() != None:
            self.as_.lea(node.memref(),reg)
        else :
            raise Exception("must not happen: constant has no asm value")
    
    def load_variable(self,var,dest):
        if var.memref() == None:
            a = des.for_type(self.ntype)
            self.as_.mov(var.address(),a)
            self.load(self.mem(a),dest.for_type(var.type()))
        else :
            self.load(var.memref(),dest.for_type(var.type()))
    
    def load_address(self,var,dest):
        if var.address() != None:
            self.as_.mov(var.address(),dest)
        else :
            self.as_.mov(var.memref(),dest)
    
    def ax(self,t=None):
        if t == None:
            return Register(RegisterClass.AX,self.ntype)
        else :
            return Register(RegisterClass.AX,t)
    
    def bx(self,t=None):
        if t == None:
            return Register(RegisterClass.BX,self.ntype)
        else :
            return Register(RegisterClass.BX,t)
    
    def cx(self,t=None):
        if t == None:
            return Register(RegisterClass.CX,self.ntype)
        else :
            return Register(RegisterClass.CX,t)
    
    def dx(self,t=None):
        if t == None:
            return Register(RegisterClass.DX,self.ntype)
        else :
            return Register(RegisterClass.DX,t)
    
    def al(self):
        return self.ax(Type.INT8)
    
    def cl(self):
        return self.cx(Type.INT8)

    def si(self):
        return Register(RegisterClass.SI, self.ntype)
    
    def di(self):
        return Register(RegisterClass.DI, self.ntype)
    
    def bp(self):
        return Register(RegisterClass.BP, self.ntype)
    
    def sp(self):
        return Register(RegisterClass.SP, self.ntype)

    def mem(self,a1,a2=None):
        if a2 == None:
            if isinstance(a1,Symbol):
                return DirectMemoryReference(a1)
            else :
                return IndirectMemoryReference(0,a1)
        else :
            return IndirectMemoryReference(a1,a2)
    
    def imm(self,n):
        return ImmediateValue(n)

    def load(self,mem,reg):
        self.as_.mov(mem,reg)
    
    def store(self,reg,mem):
        self.as_.mov(reg,mem)
        



    
    


    
    


    

    
    


    




    

