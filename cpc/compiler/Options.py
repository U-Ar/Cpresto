import re
from sysdep.X86Linux import X86Linux
from cpcparser.LibraryLoader import LibraryLoader
from sysdep.CodeGeneratorOptions import CodeGeneratorOptions
from sysdep.AssemblerOptions import AssemblerOptions
from sysdep.LinkerOptions import LinkerOptions

from exception.CompileException import CompileException

from .CompilerMode import CompilerMode
from .SourceFile import SourceFile


class Options:
    @staticmethod
    def parse(args):
        opts = Options()
        opts.parse_args(args)
        return opts
    
    

    def __init__(self):
        self._platform = X86Linux()
        self._verbose = False
        self._loader = LibraryLoader()
        self._debug_parser = False
        self._gen_options = CodeGeneratorOptions()
        self._as_options = AssemblerOptions()
        self._ld_options = LinkerOptions()

        self._mode = None
        self._output_file_name = None
        self._ld_args = []
        self._source_files = []

    def mode(self):
        return self._mode
    def is_assemble_required(self):
        return self._mode.requires(CompilerMode.Assemble)
    def is_link_required(self):
        return self._mode.requires(CompilerMode.Link)
    def source_files(self):
        return self._source_files
    
    def asm_file_name_of(self,src):
        if self._output_file_name != None and self._mode == CompilerMode.Compile:
            return self._output_file_name
        return src.asm_file_name()
    
    def obj_file_name_of(self,src):
        if self._output_file_name != None and self._mode == CompilerMode.Assemble:
            return self._output_file_name
        return src.obj_file_name()
    
    def exe_file_name(self):
        return self.linked_file_name("")
    
    def so_file_name(self):
        return self.linked_file_name(".so")
    
    DEFAULT_LINKER_OUTPUT = "a.out"

    def linked_file_name(self,new_ext):
        if self._output_file_name != None:
            return self._output_file_name
        elif len(self._source_files) == 1:
            return self._source_files[0].linked_file_name(new_ext)
        else :
            return Options.DEFAULT_LINKER_OUTPUT
    
    def output_file_name(self):
        return self._output_file_name
    def is_verbose_mode(self):
        return self._verbose
    def does_debug_parser(self):
        return self._debug_parser
    def loader(self):
        return self._loader
    def type_table(self):
        return self._platform.type_table()
    def code_generator(self,h):
        return self._platform.code_generator(self._gen_options,h)
    def assembler(self,h):
        return self._platform.assembler(h)
    def as_options(self):
        return self._as_options
    def linker(self,h):
        return self._platform.linker(h)
    def ld_options(self):
        return self._ld_options
    def ld_args(self):
        res = []
        for arg in self._ld_args:
            res.append(arg.to_string())
        return res
    def is_generating_shared_library(self):
        return self._ld_options.generating_shared_library
    
    def parse_args(self,orig_args):
        source_files = []
        ld_args = []
        i = 0
        cmodes = CompilerMode.modes()
        while i < len(orig_args):
            arg = orig_args[i]
            
            if arg == "--":
                break
            elif arg.startswith("-"):
                if arg in cmodes:
                    if self._mode != None:
                        self.parse_error(self._mode.to_option()+" option and "\
                            + arg + " option is exclusive")
                    self._mode = CompilerMode.from_option(arg)
                elif arg.startswith("-I"):
                    self._loader.add_load_path(self.get_opt_arg(arg,orig_args,i))
                elif arg == "--debug-parser":
                    self._debug_parser = True
                elif arg.startswith("-o"):
                    self._output_file_name = self.get_opt_arg(arg,orig_args,i)
                elif arg == "-fpic" or arg == "-fPIC":
                    self._gen_options.generate_PIC()
                elif arg == "-fpie" or arg == "-fPIE":
                    self._gen_options.generate_PIE()
                elif arg.startswith("-O"):
                    t = arg[2:]
                    if re.match(r"^([0123s]|)$",t) == None:
                        self.parse_error("unknown optimization switch: "+arg)
                    self._gen_options.set_optimization_level(0 if t == "0" else 1)
                elif arg == "-fverbose-asm" or arg == "--verbose-asm":
                    self._gen_options.generate_verbose_asm()
                elif arg.startswith("-Wa,"):
                    for a in self.parse_comma_separated_options(arg):
                        self._as_options.add_arg(a)
                elif arg == "-Xassembler":
                    self._as_options.add_arg(self.next_arg(arg, orig_args, i))
                elif arg == "-static":
                    self.add_ld_arg(arg)
                elif arg == "-shared":
                    self._ld_options.generating_shared_library = True
                elif arg == "-pie":
                    self._ld_options.generating_PIE = True
                elif arg == "--readonly-got":
                    self.add_ld_arg("-z")
                    self.add_ld_arg("combreloc")
                    self.add_ld_arg("-z")
                    self.add_ld_arg("now")
                    self.add_ld_arg("-z")
                    self.add_ld_arg("relro")
                elif arg.startswith("-L"):
                    self.add_ld_arg("-L"+self.get_opt_arg(arg,orig_args,i))
                elif arg.startswith("-I"):
                    self.add_ld_arg("-I"+self.get_opt_arg(arg,orig_args,i))
                elif arg == "-nostartfiles":
                    self._ld_options.no_start_files = True
                elif arg == "-nodefaultlibs":
                    self._ld_options.no_default_libs = True  
                elif arg == "-nostdlib":
                    self._ld_options.no_start_files = True
                    self._ld_options.no_default_libs = True  
                elif arg.startswith("-WL,"):
                    for o in self.parse_comma_separated_options(arg):
                        self.add_ld_arg(o)
                elif arg == "-Xlinker":
                    self.add_ld_arg(self.next_arg(arg,orig_args,i))
                elif arg == "-v":
                    self._verbose = True
                    self._as_options.verbose = True
                    self._ld_options.verbose = True
                elif arg == "--version":
                    print("{} version {}".format(Compiler.program_name,Compiler.version))
                    sys.exit(0)
                elif arg == "--help":
                    self.print_usage(sys.stdout)
                    sys.exit(0)
                else :
                    self.parse_error("unknown option: " + arg)

            else :
                ld_args.append(SourceFile(arg))
            i += 1
        
        while i < len(orig_args) - 1:
            i += 1
            ld_args.append(SourceFile(arg[i]))
        
        if self._mode == None:
            self._mode = CompilerMode.Link
        source_files = self.select_source_files(ld_args)
        if len(source_files) == 0:
            self.parse_error("no input file")
        for src in source_files:
            if not src.is_known_file_type():
                self.parse_error("unknown file type: " + src.path())
        if self._output_file_name != None and len(source_files)>1 and not self.is_link_required():
            self.parse_error("-o option requires only 1 input (except linking)")




    def parse_error(self,msg):
        raise OptionParseError(msg)
    
    def add_ld_arg(self,arg):
        self._ld_args.append(LdOption(arg))
    
    def select_source_files(self,args):
        res = []
        for arg in args:
            if arg.is_source_file():
                res.append(arg)
        return res
    
    def get_opt_arg(self,opt,args,i):
        path = opt[2:]
        if len(path) != 0:
            return path
        else :
            return self.next_arg(opt,args,i)
    
    def next_arg(self,opt, args,i):
        if len(args) - 1 <= i:
            self.parse_error("missing argument for" + opt)
        return args[i+1]

    def parse_comma_separated_options(self,opt):
        opts = opt.split(",")
        if len(opts) <= 1:
            self.parse_error("missing argument for "+opt)
        res = []
        for i in range(1,len(opts)):
            res.append(opts[i])
        return res


    def print_usage(self,out):
        out.write("Usage: cbc [options] file...\n")
        out.write("Global Options:\n")
        out.write("  --check-syntax   Checks syntax and quit.\n")
        out.write("  --dump-tokens    Dumps tokens and quit.\n")
        # --dump-stmt is a hidden option.
        # --dump-expr is a hidden option.
        out.write("  --dump-ast       Dumps AST and quit.\n")
        out.write("  --dump-semantic  Dumps AST after semantic checks and quit.\n")
        # --dump-reference is a hidden option.
        out.write("  --dump-ir        Dumps IR and quit.\n")
        out.write("  --dump-asm       Dumps AssemblyCode and quit.\n")
        out.write("  --print-asm      Prints assembly code and quit.\n")
        out.write("  -S               Generates an assembly file and quit.\n")
        out.write("  -c               Generates an object file and quit.\n")
        out.write("  -o PATH          Places output in file PATH.\n")
        out.write("  -v               Turn on verbose mode.\n")
        out.write("  --version        Shows compiler version and quit.\n")
        out.write("  --help           Prints this message and quit.\n")
        out.write("\n")
        out.write("Optimization Options:\n")
        out.write("  -O               Enables optimization.\n")
        out.write("  -O1, -O2, -O3    Equivalent to -O.\n")
        out.write("  -Os              Equivalent to -O.\n")
        out.write("  -O0              Disables optimization (default).\n")
        out.write("\n")
        out.write("Parser Options:\n")
        out.write("  -I PATH          Adds PATH as import file directory.\n")
        out.write("  --debug-parser   Dumps parsing process.\n")
        out.write("\n")
        out.write("Code Generator Options:\n")
        out.write("  -O               Enables optimization.\n")
        out.write("  -O1, -O2, -O3    Equivalent to -O.\n")
        out.write("  -Os              Equivalent to -O.\n")
        out.write("  -O0              Disables optimization (default).\n")
        out.write("  -fPIC            Generates PIC assembly.\n")
        out.write("  -fpic            Equivalent to -fPIC.\n")
        out.write("  -fPIE            Generates PIE assembly.\n")
        out.write("  -fpie            Equivalent to -fPIE.\n")
        out.write("  -fverbose-asm    Generate assembly with verbose comments.\n")
        out.write("\n")
        out.write("Assembler Options:\n")
        out.write("  -Wa,OPT          Passes OPT to the assembler (as).\n")
        out.write("  -Xassembler OPT  Passes OPT to the assembler (as).\n")
        out.write("\n")
        out.write("Linker Options:\n")
        out.write("  -l LIB           Links the library LIB.\n")
        out.write("  -L PATH          Adds PATH as library directory.\n")
        out.write("  -shared          Generates shared library rather than executable.\n")
        out.write("  -static          Linkes only with static libraries.\n")
        out.write("  -pie             Generates PIE.\n")
        out.write("  --readonly-got   Generates read-only GOT (ld -z combreloc -z now -z relro).\n")
        out.write("  -nostartfiles    Do not link startup files.\n")
        out.write("  -nodefaultlibs   Do not link default libraries.\n")
        out.write("  -nostdlib        Enables -nostartfiles and -nodefaultlibs.\n")
        out.write("  -Wl,OPT          Passes OPT to the linker (ld).\n")
        out.write("  -Xlinker OPT     Passes OPT to the linker (ld).\n")
    