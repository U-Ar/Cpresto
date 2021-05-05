import sys
from antlr4 import *
from HelloLexer import HelloLexer
from HelloParser import HelloParser

def main(argv):
    input_stream = FileStream(argv[1],encoding="utf-8")
    lexer = HelloLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.parse()
    print(tree.toStringTree(recog=parser))

if __name__ == "__main__":
    main(sys.argv)