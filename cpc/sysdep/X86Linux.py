from .Platform import Platform
from .GNUAssembler import GNUAssembler
from .GNULinker import GNULinker
from type.TypeTable import TypeTable
import x86.CodeGenerator
from asm.Type import Type

class X86Linux(Platform):
    def type_table(self):
        return TypeTable.ilp32
    
    def code_generator(self,opts,h):
        return x86.CodeGenerator(opts,self.natural_type(),h)
    
    def natural_type(self):
        return Type.INT32
    
    def assembler(self,h):
        return GNUAssembler(h)

    def linker(self,h):
        return GNULinker(h)
