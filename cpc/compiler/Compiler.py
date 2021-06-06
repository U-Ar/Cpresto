import sys

from .CompilerMode import CompilerMode
from .DereferenceChecker import DereferenceChecker
from .IRGenerator import IRGenerator
from .LdOption import LdOption
from .LocalResolver import LocalResolver
from .Options import Options
from .SourceFile import SourceFile
from .TypeChecker import TypeChecker
from .TypeResolver import TypeResolver
from cpcparser.WrappedParser import WrappedParser
from utils.ErrorHandler import ErrorHandler
from exception.OptionParseError import OptionParseError
from exception.CompileException import CompileException
from exception.FileException import FileException

class Compiler:
    program_name = "cpc"
    version = "1.0.0"

    @staticmethod
    def main(args):
        Compiler(Compiler.program_name).command_main(args)
    
    def __init__(self,program_name):
        self.error_handler = ErrorHandler(program_name)

    
    def command_main(self,args):
        opts = self.parse_options(args)
        if opts.mode() == CompilerMode.CheckSyntax:
            sys.exit(0 if self.check_syntax(opts) else 1)
        try:
            srcs = opts.source_files()
            self.build(srcs, opts)
            sys.exit(0)
        except CompileException as ex:
            self.error_handler.error(ex.message)
            sys.exit(1)
    
    def parse_options(self,args):
        try:
            return Options.parse(args)
        except OptionParseError as ex:
            self.error_handler.error(ex.message)
            self.error_handler.error("Try \"cpc --help\" for usage")
            sys.exit(1)
            return None
    
    def check_syntax(self,opts):
        failed = False
        for src in opts.source_files():
            if self.is_valid_syntax(src.path(),opts):
                print(src.path()+": Syntax OK")
            else :
                print(src.path()+": Syntax Error")
                failed = True
        return not failed

    def is_valid_syntax(self,path,opts):
        try:
            self.parse_file(path,opts)
            return True
        except SyntaxException as ex:
            return False
        except FileException as ex:
            self.error_handler.error(ex.message)
            return False
    
    def build(self,srcs,opts):
        for src in srcs:
            if src.is_Cpresto_source():
                dest = opts.asm_file_name_of(src)
                self.compile(src.path(),dest,opts)
                src.set_current_name(dest)
            if not opts.is_assemble_required():
                continue
            if src.is_assembly_source():
                dest = opts.obj_file_name_of(src)
                self.assemble(src,path(),dest,opts)
                src.set_current_name(dest)
        if not opts.is_link_required():
            return 
        self.link(opts)
    
    def compile(self,srcpath,destpath,opts):
        ast = self.parse_file(srcpath,opts).res
        if self.dump_AST(ast,opts.mode()):
            return 
        types = opts.type_table()
        sem = self.semantic_analyze(ast,types,opts)
        if self.dump_semant(sem, opts.mode()):
            return
        ir = IRGenerator(types,self.error_handler).generate(sem)
        if self.dump_IR(ir,opts.mode()):
            return
        asm = self.generate_assembly(ir,opts)
        if self.dump_asm(asm,opts.mode()):
            return
        if self.print_asm(asm,opts.mode()):
            return
        self.write_file(destpath,asm.to_source())
    
    def parse_file(self,path,opts):
        return WrappedParser.parse_file(path,opts.loader(),self.error_handler,opts.does_debug_parser())

    def semantic_analyze(self,ast,types,opts):
        LocalResolver(self.error_handler).resolve(ast)
        TypeResolver(types,self.error_handler).resolve(ast)
        types.semantic_check(self.error_handler)
        if opts.mode() == CompilerMode.DumpReference:
            ast.dump()
            return ast
        DereferenceChecker(types,self.error_handler).check(ast)
        TypeChecker(types,self.error_handler).check(ast)
        return ast
    
    def generate_assembly(self,ir,opts):
        return opts.code_generator(self.error_handler).generate(ir)
    
    def assemble(self,srcpath,destpath,opts):
        opts.assembler(self.error_handler).assemble(srcpath,destpath,opts.as_options())

    def link(self,opts):
        if not opts.is_generating_shared_library():
            self.generate_executable(opts)
        else:
            self.generate_shared_library(opts)
    
    def generate_executable(self,opts):
        opts.linker(self.error_handler).generate_executable(opts.ld_args(),opts.exe_file_name(),opts.ld_options())
    
    def generate_shared_library(self,opts):
        opts.linker(self.error_handler).generate_shared_library(opts.ld_args(),opts.so_file_name(),opts.ld_options())

    def write_file(self,path,s):
        if path == "-":
            sys.stdout.write(s)
            return
        try:
            f = open(path, "w")
            try :
                f.write(s)
            finally :
                f.close()
        except FileNotFoundError as ex:
            self.error_handler.error("file not found: "+path)
        except OSError as ex:
            self.error_handler.error("OS error"+ex.message)
            raise FileException("file error")

    def dump_AST(self,ast,mode):
        if mode == CompilerMode.DumpTokens:
            ast.dump_tokens(sys.stdout)
            return True
        elif mode == CompilerMode.DumpAST:
            ast.dump()
            return True
        elif mode == CompilerMode.DumpStmt:
            self.find_stmt(ast).dump()
            return True
        elif mode == CompilerMode.DumpExpr:
            self.find_expr(ast).dump()
            return True
        else :
            return False
        
    def find_stmt(self,ast):
        stmt = ast.get_single_main_stmt()
        if stmt == None:
            self.error_exit("source file does not contains main()")
        return stmt
    
    def find_expr(self,ast):
        expr = ast.get_single_main_expr()
        if expr == None:
            self.error_exit("source file does not contains single expression")
        return expr

    def dump_semant(self,ast,mode):
        if mode == CompilerMode.DumpReference:
            return True
        elif mode == CompilerMode.DumpSemantic:
            ast.dump()
            return True
        else :
            return False
        
    def dump_IR(self,ir,mode):
        if mode == CompilerMode.DumpIR:
            ir.dump()
            return True
        else :
            return False

    def dump_asm(self,asm,mode):
        if mode == CompilerMode.DumpAsm:
            asm.dump(sys.stdout)
            return True
        else :
            return False
    
    def print_asm(self,asm,mode):
        if mode == CompilerMode.PrintAsm:
            sys.stdout.write(asm.to_source())
            return True
        else :
            return False

    def error_exit(self,msg):
        self.error_handler.error(msg)
        sys.exit(1)

