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
    
    def generate(self,ir):
        self.locate_symbols(ir)
        return self.generate_assembly_code(ir)
    
    LABEL_SYMBOL_BASE = ".L"
    CONST_SYMBOL_BASE = ".LC"
    STACK_WORD_SIZE = 4
    GOT = NamedSymbol("_GLOVAL_OFFSET_TABLE_")

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

    

    
    


    




    

