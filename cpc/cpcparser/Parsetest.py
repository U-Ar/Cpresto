import sys
from antlr4 import *
from CprestoLexer import CprestoLexer
from CprestoParser import CprestoParser
from WrappedParser import WrappedParser
from LibraryLoader import LibraryLoader
def main(argv):
    #input_stream = FileStream(argv[1])
    #lexer = CprestoLexer(input_stream)
    #stream = CommonTokenStream(lexer)
    #parser = CprestoParser(stream)
    print("loaded file: ",argv[1])
    print()
    parser = WrappedParser.new_file_parser(argv[1],LibraryLoader(),None,None)
    tree = parser.compilation_unit() #トップレベルのトークン 
    print(tree.toStringTree(recog=parser))
if __name__ == "__main__":
    sys.path.append("../")
    main(sys.argv)
