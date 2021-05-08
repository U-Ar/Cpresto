from .Linker import Linker
from utils.CommandUtils import CommandUtils

class GNULinker(Linker):
    # 32bit Linux dependent
    LINKER = "/usr/bin/ld"
    DYNAMIC_LINKER      = "/lib/ld-linux.so.2"
    C_RUNTIME_INIT      = "/usr/lib/crti.o"
    C_RUNTIME_START     = "/usr/lib/crt1.o"
    C_RUNTIME_START_PIE = "/usr/lib/Scrt1.o"
    C_RUNTIME_FINI      = "/usr/lib/crtn.o"

    def __init__(self,error_handler):
        self.error_handler = error_handler

    def generate_executable(self,args,destpath,opts):
        cmd = []
        cmd.append(GNULinker.LINKER)
        cmd.append("-dynamic-linker")
        cmd.append(GNULinker.DYNAMIC_LINKER)
        if opts.generating_PIE:
            cmd.append("-pie")
        if not opts.no_start_files:
            if opts.generating_PIE:
                cmd.append(GNULinker.C_RUNTIME_START_PIE)
            else:
                cmd.append(GNULinker.C_RUNTIME_START)
            cmd.append(GNULinker.C_RUNTIME_INIT)
        cmd += args
        if not opts.no_default_libs:
            cmd.append("-lc")
            cmd.append("-lcbc")
        if not opts.no_start_files:
            cmd.append(GNULinker.C_RUNTIME_FINI)
        cmd.append("-o")
        cmd.append(destpath)
        CommandUtils.invoke(cmd,self.error_handler,opts.verbose)
    
    def generate_shared_library(self,args,destpath,opts):
        cmd = []
        cmd.append(GNULinker.LINKER)
        cmd.append("-shared")
        if not opts.no_start_files:
            cmd.append(GNULinker.C_RUNTIME_INIT)
        cmd += args
        if not opts.no_default_libs:
            cmd.append("-lc")
            cmd.append("-lcbc")
        if not opts.no_start_files:
            cmd.append(GNULinker.C_RUNTIME_FINI)
        cmd.append("-o")
        cmd.append(destpath)
        CommandUtils.invoke(cmd,self.error_handler,opts.verbose)