from enum import Enum

class CompilerMode(Enum):
    CheckSyntax = 0#"--check-syntax"
    DumpTokens = 1#"--dump-tokens"
    DumpAST = 2#"--dump-ast"
    DumpStmt = 3#"--dump-stmt"
    DumpExpr = 4#"--dump-expr"
    DumpSemantic = 5#"--dump-semantic"
    DumpReference = 6#"--dump-reference"
    DumpIR = 7#"--dump-ir"
    DumpAsm = 8#"--dump-asm"
    PrintAsm = 9#"--print-asm"
    Compile = 10#"-S"
    Assemble = 11#"-c"
    Link = 12#"--link"


    @staticmethod
    def modes():
        return {"--check-syntax": CompilerMode.CheckSyntax,
             "--dump-tokens":  CompilerMode.DumpTokens,
             "--dump-ast": CompilerMode.DumpAST,
            "--dump-stmt": CompilerMode.DumpStmt,
            "--dump-expr": CompilerMode.DumpExpr,
            "--dump-semantic": CompilerMode.DumpSemantic,
            "--dump-reference": CompilerMode.DumpReference,
            "--dump-ir": CompilerMode.DumpIR,
            "--dump-asm": CompilerMode.DumpAsm,
            "--print-asm": CompilerMode.PrintAsm,
            "-S": CompilerMode.Compile,
            "-c": CompilerMode.Assemble }
    
    @staticmethod
    def is_mode_option(opt):
        return opt in CompilerMode.modes()
    
    @staticmethod
    def from_option(opt):
        mod = CompilerMode.modes()
        if opt not in mod:
            raise Exception("must not happen: unkown mode option: " + opt)
        return mod[opt]
    
    def __init__(self,option):
        self._option = option
    
    def to_option(self):
        return self._option
    
    def requires(self,m):
        return self.value >= m.value


    