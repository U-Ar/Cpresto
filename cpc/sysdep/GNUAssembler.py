from .Assembler import Assembler
from utils.CommandUtils import CommandUtils

class GNUAssembler(Assembler):
    def __init__(self,h):
        self.error_handler = h
    
    def assemble(self,srcpath,destpath,opts):
        cmd = []
        cmd.append("as")
        cmd += opts.args
        cmd.append("-o")
        cmd.append(destpath)
        cmd.append(srcpath)
        CommandUtils.invoke(cmd,self.error_handler,opts.verbose)