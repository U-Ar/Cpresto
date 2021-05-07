from CprestoParser import CprestoParser
from CprestoLexer import CprestoLexer
from antlr4 import *

class WrappedParser(CprestoParser):
    @staticmethod
    def parse_file(file,loader,error_handler,debug=None):
            if debug == None:
                    debug = False
            return Parser.new_file_parser(file,loader,error_handler,debug).parse()

    @staticmethod
    def parse_decl_file(file,loader,error_handler,debug=None):
            if debug == None:
                    debug = False
            return Parser.new_file_parser(file,loader,error_handler,debug).parse_decls()

    @staticmethod
    def new_file_parser(filename,loader,error_handler,debug):
            try:
                    input_stream = FileStream(filename)
                    lexer = CprestoLexer(input_stream)
                    stream = CommonTokenStream(lexer)
                    return WrappedParser(stream,filename,loader,error_handler,debug)
            except FileNotFoundError as ex:
                    raise FileException(ex.message)
            except Exception as ex:
                    raise Exception("UTF-8 is not supported?: "+ex.message)
    
    def __init__(self,s,name,loader,error_handler,debug=None):
        super().__init__(s)
        self.token_stream = s
        self.source_name = name
        self.loader = loader
        self.error_handler = error_handler
        self.known_typedefs = set()
    