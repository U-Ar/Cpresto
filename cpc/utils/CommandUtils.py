import sys
import subprocess
import io
from subprocess import PIPE
from exception.IPCException import IPCException

class CommandUtils:
    @staticmethod
    def invoke(cmd_args,error_handler,verbose):
        if verbose:
            CommandUtils.dump_command(cmd_args)
        try:
            proc = subprocess.run(cmd_args,stdout=PIPE,stderr=PIPE,universal_newlines=True)
            CommandUtils.pass_through(io.StringIO(proc.stdout))
            CommandUtils.pass_through(io.StringIO(proc.stderr))
            if proc.returncode != 0:
                error_handler(cmd_args[0] + " failed."\
                    +" (status "+str(proc.returncode)+")")
                raise IPCException("compile error")
        except InterruptedError as ex:
            error_handler.error("external command interrupted: "\
                                + cmd_args[0] + ": " +ex.message)
            raise IPCException("compile error")
        except Exception as ex:
            error_handler.error("IO error? in external command: "\
                + ex.message)
            raise IPCException("compile error")

    @staticmethod
    def dump_command(args):
        sep = ""
        for arg in args:
            print(sep, file=sys.stdout)
            sep = " "
            print(arg, file=sys.stdout)
        print("",file=sys.stdout)

    @staticmethod
    def pass_through(s):
        line=s.readline()
        while line != "":
            print(line, file=sys.stderr)
            line = s.readline()