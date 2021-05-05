import sys
from antlr4 import *
from CprestoLexer import CprestoLexer
from CprestoParser import CprestoParser
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = CprestoLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CprestoParser(stream)
    tree = parser.compilation_unit() #トップレベルのトークン 
    print(tree.toStringTree(recog=parser))
if __name__ == "__main__":
    main(sys.argv)
