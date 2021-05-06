# Generated from c:\codes\Cpresto\cpc\parser\Cpresto.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


import sys
sys.path.append('../')
import abst
"""from ..ast.AbstractAssignNode import *
from ..ast.AddressNode import *
from ..ast.ArefNode import *
from ..ast.AssignNode import *
from ..ast.AST import *
from ..ast.ASTVisitor import *
from ..ast.BinaryOpNode import *
from ..ast.BlockNode import *
from ..ast.BreakNode import *
from ..ast.CaseNode import *
from ..ast.CastNode import *
from ..ast.CflatToken import *
from ..ast.CompositeTypeDefinition import *
from ..ast.CondExprNode import *
from ..ast.ContinueNode import *
from ..ast.Declarations import *
from ..ast.DeclarationVisitor import *
from ..ast.DereferenceNode import *
from ..ast.DoWhileNode import *
from ..ast.Dumpable import *
from ..ast.Dumper import *
from ..ast.ExprNode import *
from ..ast.ExprStmtNode import *
from ..ast.ForNode import *
from ..ast.FuncallNode import *
from ..ast.GotoNode import *
from ..ast.IfNode import *
from ..ast.IntegerLiteralNode import *
from ..ast.LabelNode import *
from ..ast.LHSNode import *
from ..ast.LiteralNode import *
from ..ast.Location import *
from ..ast.LogicalAndNode import *
from ..ast.LogicalOrNode import *
from ..ast.MemberNode import *
from ..ast.Node import *
from ..ast.OpAssignNode import *
from ..ast.PrefixOpNode import *
from ..ast.PtrMemberNode import *
from ..ast.ReturnNode import *
from ..ast.SizeofExprNode import *
from ..ast.SizeofTypeNode import *
from ..ast.Slot import *
from ..ast.StmtNode import *
from ..ast.StringLiteralNode import *
from ..ast.StructNode import *
from ..ast.SuffixOpNode import *
from ..ast.SwitchNode import *
from ..ast.TypeDefinition import *
from ..ast.TypedefNode import *
from ..ast.TypeNode import *
from ..ast.UnaryArithmeticOpNode import *
from ..ast.UnaryOpNode import *
from ..ast.UnionNode import *
from ..ast.VariableNode import *
from ..ast.WhileNode import *

from ..entity.Constant import *
from ..entity.ConstantEntity import *
from ..entity.ConstantTable import *
from ..entity.DefinedFunction import *
from ..entity.DefinedVariable import *
from ..entity.Entity import *
from ..entity.EntityVisitor import *
from ..entity.Function import *
from ..entity.LocalScope import *
from ..entity.Parameter import *
from ..entity.Params import *
from ..entity.ParamSlots import *
from ..entity.Scope import *
from ..entity.ToplevelScope import *
from ..entity.UndefinedFunction import *
from ..entity.UndefinedVariable import *
from ..entity.Variable import *

from ..type.ArrayType import *
from ..type.ArrayTypeRef import *
from ..type.CompositeType import *
from ..type.FunctionType import *
from ..type.FunctionTypeRef import *
from ..type.IntegerType import *
from ..type.IntegerTypeRef import *
from ..type.NamedType import *
from ..type.ParamTypeRefs import *
from ..type.ParamTypes import *
from ..type.PointerType import *
from ..type.PointerTypeRef import *
from ..type.StructType import *
from ..type.StructTypeRef import *
from ..type.Type import *
from ..type.TypeRef import *
from ..type.TypeTable import *
from ..type.UnionType import *
from ..type.UnionTypeRef import *
from ..type.UserType import *
from ..type.UserTypeRef import *
from ..type.VoidType import *
from ..type.VoidTypeRef import *

from ..asm.Label import Label
from ..utils.ErrorHandler import ErrorHandler

from ..exception.CompileException import *
from ..exception.FileException import *
from ..exception.IPCException import *
from ..exception.JumpError import *
from ..exception.OptionParseError import *
from ..exception.SemanticError import *
from ..exception.SemanticException import *
from ..exception.SyntaxException import *"""




def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2S")
        buf.write("\u0228\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2\3\2\3\3\3\3")
        buf.write("\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\33\3\33\3\33\3\34\3\34\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3")
        buf.write("#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)\3)\3*\3")
        buf.write("*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38")
        buf.write("\38\39\39\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3>\3>\3")
        buf.write(">\3>\3>\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3A\3A\3A\3")
        buf.write("A\3A\3A\3A\3A\3B\3B\3B\3B\3B\3B\3C\3C\3C\3D\3D\3D\3D\3")
        buf.write("E\3E\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3")
        buf.write("G\3G\3G\3G\3H\3H\3H\3H\3H\3I\3I\3I\3I\3I\3I\3I\3I\3J\3")
        buf.write("J\3J\3J\3J\3J\3J\3K\3K\3K\3K\3K\3K\3K\3L\3L\7L\u01c6\n")
        buf.write("L\fL\16L\u01c9\13L\3M\3M\7M\u01cd\nM\fM\16M\u01d0\13M")
        buf.write("\3M\5M\u01d3\nM\3M\5M\u01d6\nM\3M\3M\3M\6M\u01db\nM\r")
        buf.write("M\16M\u01dc\3M\5M\u01e0\nM\3M\5M\u01e3\nM\3M\3M\7M\u01e7")
        buf.write("\nM\fM\16M\u01ea\13M\3M\5M\u01ed\nM\3M\5M\u01f0\nM\5M")
        buf.write("\u01f2\nM\3N\6N\u01f5\nN\rN\16N\u01f6\3N\3N\3O\3O\3O\3")
        buf.write("O\7O\u01ff\nO\fO\16O\u0202\13O\3O\3O\3O\3O\5O\u0208\n")
        buf.write("O\3P\3P\3P\3P\7P\u020e\nP\fP\16P\u0211\13P\3P\3P\3P\3")
        buf.write("Q\3Q\3Q\3Q\7Q\u021a\nQ\fQ\16Q\u021d\13Q\3Q\3Q\3R\3R\3")
        buf.write("R\3R\5R\u0225\nR\3R\3R\4\u020f\u021b\2S\3\3\5\4\7\5\t")
        buf.write("\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20")
        buf.write("\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65")
        buf.write("\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60")
        buf.write("_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>{?}@\177A\u0081")
        buf.write("B\u0083C\u0085D\u0087E\u0089F\u008bG\u008dH\u008fI\u0091")
        buf.write("J\u0093K\u0095L\u0097M\u0099N\u009bO\u009dP\u009fQ\u00a1")
        buf.write("R\u00a3S\3\2\f\5\2C\\aac|\6\2\62;C\\aac|\3\2\63;\3\2\62")
        buf.write(";\4\2ZZzz\5\2\62;CHch\3\2\629\5\2\13\f\16\17\"\"\4\2\f")
        buf.write("\f\17\17\3\2^^\2\u023c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2")
        buf.write("\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2")
        buf.write("\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2")
        buf.write("\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\3\u00a5\3\2\2\2\5\u00a7\3\2\2\2\7\u00a9")
        buf.write("\3\2\2\2\t\u00ab\3\2\2\2\13\u00ad\3\2\2\2\r\u00af\3\2")
        buf.write("\2\2\17\u00b1\3\2\2\2\21\u00b5\3\2\2\2\23\u00b7\3\2\2")
        buf.write("\2\25\u00b9\3\2\2\2\27\u00bb\3\2\2\2\31\u00bd\3\2\2\2")
        buf.write("\33\u00bf\3\2\2\2\35\u00c1\3\2\2\2\37\u00c4\3\2\2\2!\u00c7")
        buf.write("\3\2\2\2#\u00ca\3\2\2\2%\u00cd\3\2\2\2\'\u00d0\3\2\2\2")
        buf.write(")\u00d3\3\2\2\2+\u00d6\3\2\2\2-\u00d9\3\2\2\2/\u00dd\3")
        buf.write("\2\2\2\61\u00e1\3\2\2\2\63\u00e3\3\2\2\2\65\u00e6\3\2")
        buf.write("\2\2\67\u00e9\3\2\2\29\u00eb\3\2\2\2;\u00ed\3\2\2\2=\u00f0")
        buf.write("\3\2\2\2?\u00f3\3\2\2\2A\u00f6\3\2\2\2C\u00f9\3\2\2\2")
        buf.write("E\u00fb\3\2\2\2G\u00fd\3\2\2\2I\u00ff\3\2\2\2K\u0102\3")
        buf.write("\2\2\2M\u0105\3\2\2\2O\u0107\3\2\2\2Q\u0109\3\2\2\2S\u010b")
        buf.write("\3\2\2\2U\u010d\3\2\2\2W\u0110\3\2\2\2Y\u0113\3\2\2\2")
        buf.write("[\u0115\3\2\2\2]\u0117\3\2\2\2_\u011a\3\2\2\2a\u011f\3")
        buf.write("\2\2\2c\u0124\3\2\2\2e\u012a\3\2\2\2g\u012e\3\2\2\2i\u0133")
        buf.write("\3\2\2\2k\u013a\3\2\2\2m\u0140\3\2\2\2o\u0145\3\2\2\2")
        buf.write("q\u014c\3\2\2\2s\u0153\3\2\2\2u\u0159\3\2\2\2w\u0160\3")
        buf.write("\2\2\2y\u0169\3\2\2\2{\u016c\3\2\2\2}\u0171\3\2\2\2\177")
        buf.write("\u0178\3\2\2\2\u0081\u017d\3\2\2\2\u0083\u0185\3\2\2\2")
        buf.write("\u0085\u018b\3\2\2\2\u0087\u018e\3\2\2\2\u0089\u0192\3")
        buf.write("\2\2\2\u008b\u0199\3\2\2\2\u008d\u019f\3\2\2\2\u008f\u01a8")
        buf.write("\3\2\2\2\u0091\u01ad\3\2\2\2\u0093\u01b5\3\2\2\2\u0095")
        buf.write("\u01bc\3\2\2\2\u0097\u01c3\3\2\2\2\u0099\u01f1\3\2\2\2")
        buf.write("\u009b\u01f4\3\2\2\2\u009d\u01fa\3\2\2\2\u009f\u0209\3")
        buf.write("\2\2\2\u00a1\u0215\3\2\2\2\u00a3\u0220\3\2\2\2\u00a5\u00a6")
        buf.write("\7\60\2\2\u00a6\4\3\2\2\2\u00a7\u00a8\7=\2\2\u00a8\6\3")
        buf.write("\2\2\2\u00a9\u00aa\7*\2\2\u00aa\b\3\2\2\2\u00ab\u00ac")
        buf.write("\7+\2\2\u00ac\n\3\2\2\2\u00ad\u00ae\7?\2\2\u00ae\f\3\2")
        buf.write("\2\2\u00af\u00b0\7.\2\2\u00b0\16\3\2\2\2\u00b1\u00b2\7")
        buf.write("\60\2\2\u00b2\u00b3\7\60\2\2\u00b3\u00b4\7\60\2\2\u00b4")
        buf.write("\20\3\2\2\2\u00b5\u00b6\7}\2\2\u00b6\22\3\2\2\2\u00b7")
        buf.write("\u00b8\7\177\2\2\u00b8\24\3\2\2\2\u00b9\u00ba\7]\2\2\u00ba")
        buf.write("\26\3\2\2\2\u00bb\u00bc\7_\2\2\u00bc\30\3\2\2\2\u00bd")
        buf.write("\u00be\7,\2\2\u00be\32\3\2\2\2\u00bf\u00c0\7<\2\2\u00c0")
        buf.write("\34\3\2\2\2\u00c1\u00c2\7-\2\2\u00c2\u00c3\7?\2\2\u00c3")
        buf.write("\36\3\2\2\2\u00c4\u00c5\7/\2\2\u00c5\u00c6\7?\2\2\u00c6")
        buf.write(" \3\2\2\2\u00c7\u00c8\7,\2\2\u00c8\u00c9\7?\2\2\u00c9")
        buf.write("\"\3\2\2\2\u00ca\u00cb\7\61\2\2\u00cb\u00cc\7?\2\2\u00cc")
        buf.write("$\3\2\2\2\u00cd\u00ce\7\'\2\2\u00ce\u00cf\7?\2\2\u00cf")
        buf.write("&\3\2\2\2\u00d0\u00d1\7(\2\2\u00d1\u00d2\7?\2\2\u00d2")
        buf.write("(\3\2\2\2\u00d3\u00d4\7~\2\2\u00d4\u00d5\7?\2\2\u00d5")
        buf.write("*\3\2\2\2\u00d6\u00d7\7`\2\2\u00d7\u00d8\7?\2\2\u00d8")
        buf.write(",\3\2\2\2\u00d9\u00da\7>\2\2\u00da\u00db\7>\2\2\u00db")
        buf.write("\u00dc\7?\2\2\u00dc.\3\2\2\2\u00dd\u00de\7@\2\2\u00de")
        buf.write("\u00df\7@\2\2\u00df\u00e0\7?\2\2\u00e0\60\3\2\2\2\u00e1")
        buf.write("\u00e2\7A\2\2\u00e2\62\3\2\2\2\u00e3\u00e4\7~\2\2\u00e4")
        buf.write("\u00e5\7~\2\2\u00e5\64\3\2\2\2\u00e6\u00e7\7(\2\2\u00e7")
        buf.write("\u00e8\7(\2\2\u00e8\66\3\2\2\2\u00e9\u00ea\7@\2\2\u00ea")
        buf.write("8\3\2\2\2\u00eb\u00ec\7>\2\2\u00ec:\3\2\2\2\u00ed\u00ee")
        buf.write("\7@\2\2\u00ee\u00ef\7?\2\2\u00ef<\3\2\2\2\u00f0\u00f1")
        buf.write("\7>\2\2\u00f1\u00f2\7?\2\2\u00f2>\3\2\2\2\u00f3\u00f4")
        buf.write("\7?\2\2\u00f4\u00f5\7?\2\2\u00f5@\3\2\2\2\u00f6\u00f7")
        buf.write("\7#\2\2\u00f7\u00f8\7?\2\2\u00f8B\3\2\2\2\u00f9\u00fa")
        buf.write("\7~\2\2\u00faD\3\2\2\2\u00fb\u00fc\7`\2\2\u00fcF\3\2\2")
        buf.write("\2\u00fd\u00fe\7(\2\2\u00feH\3\2\2\2\u00ff\u0100\7@\2")
        buf.write("\2\u0100\u0101\7@\2\2\u0101J\3\2\2\2\u0102\u0103\7>\2")
        buf.write("\2\u0103\u0104\7>\2\2\u0104L\3\2\2\2\u0105\u0106\7-\2")
        buf.write("\2\u0106N\3\2\2\2\u0107\u0108\7/\2\2\u0108P\3\2\2\2\u0109")
        buf.write("\u010a\7\61\2\2\u010aR\3\2\2\2\u010b\u010c\7\'\2\2\u010c")
        buf.write("T\3\2\2\2\u010d\u010e\7-\2\2\u010e\u010f\7-\2\2\u010f")
        buf.write("V\3\2\2\2\u0110\u0111\7/\2\2\u0111\u0112\7/\2\2\u0112")
        buf.write("X\3\2\2\2\u0113\u0114\7#\2\2\u0114Z\3\2\2\2\u0115\u0116")
        buf.write("\7\u0080\2\2\u0116\\\3\2\2\2\u0117\u0118\7/\2\2\u0118")
        buf.write("\u0119\7@\2\2\u0119^\3\2\2\2\u011a\u011b\7x\2\2\u011b")
        buf.write("\u011c\7q\2\2\u011c\u011d\7k\2\2\u011d\u011e\7f\2\2\u011e")
        buf.write("`\3\2\2\2\u011f\u0120\7e\2\2\u0120\u0121\7j\2\2\u0121")
        buf.write("\u0122\7c\2\2\u0122\u0123\7t\2\2\u0123b\3\2\2\2\u0124")
        buf.write("\u0125\7u\2\2\u0125\u0126\7j\2\2\u0126\u0127\7q\2\2\u0127")
        buf.write("\u0128\7t\2\2\u0128\u0129\7v\2\2\u0129d\3\2\2\2\u012a")
        buf.write("\u012b\7k\2\2\u012b\u012c\7p\2\2\u012c\u012d\7v\2\2\u012d")
        buf.write("f\3\2\2\2\u012e\u012f\7n\2\2\u012f\u0130\7q\2\2\u0130")
        buf.write("\u0131\7p\2\2\u0131\u0132\7i\2\2\u0132h\3\2\2\2\u0133")
        buf.write("\u0134\7u\2\2\u0134\u0135\7v\2\2\u0135\u0136\7t\2\2\u0136")
        buf.write("\u0137\7w\2\2\u0137\u0138\7e\2\2\u0138\u0139\7v\2\2\u0139")
        buf.write("j\3\2\2\2\u013a\u013b\7w\2\2\u013b\u013c\7p\2\2\u013c")
        buf.write("\u013d\7k\2\2\u013d\u013e\7q\2\2\u013e\u013f\7p\2\2\u013f")
        buf.write("l\3\2\2\2\u0140\u0141\7g\2\2\u0141\u0142\7p\2\2\u0142")
        buf.write("\u0143\7w\2\2\u0143\u0144\7o\2\2\u0144n\3\2\2\2\u0145")
        buf.write("\u0146\7u\2\2\u0146\u0147\7v\2\2\u0147\u0148\7c\2\2\u0148")
        buf.write("\u0149\7v\2\2\u0149\u014a\7k\2\2\u014a\u014b\7e\2\2\u014b")
        buf.write("p\3\2\2\2\u014c\u014d\7g\2\2\u014d\u014e\7z\2\2\u014e")
        buf.write("\u014f\7v\2\2\u014f\u0150\7g\2\2\u0150\u0151\7t\2\2\u0151")
        buf.write("\u0152\7p\2\2\u0152r\3\2\2\2\u0153\u0154\7e\2\2\u0154")
        buf.write("\u0155\7q\2\2\u0155\u0156\7p\2\2\u0156\u0157\7u\2\2\u0157")
        buf.write("\u0158\7v\2\2\u0158t\3\2\2\2\u0159\u015a\7u\2\2\u015a")
        buf.write("\u015b\7k\2\2\u015b\u015c\7i\2\2\u015c\u015d\7p\2\2\u015d")
        buf.write("\u015e\7g\2\2\u015e\u015f\7f\2\2\u015fv\3\2\2\2\u0160")
        buf.write("\u0161\7w\2\2\u0161\u0162\7p\2\2\u0162\u0163\7u\2\2\u0163")
        buf.write("\u0164\7k\2\2\u0164\u0165\7i\2\2\u0165\u0166\7p\2\2\u0166")
        buf.write("\u0167\7g\2\2\u0167\u0168\7f\2\2\u0168x\3\2\2\2\u0169")
        buf.write("\u016a\7k\2\2\u016a\u016b\7h\2\2\u016bz\3\2\2\2\u016c")
        buf.write("\u016d\7g\2\2\u016d\u016e\7n\2\2\u016e\u016f\7u\2\2\u016f")
        buf.write("\u0170\7g\2\2\u0170|\3\2\2\2\u0171\u0172\7u\2\2\u0172")
        buf.write("\u0173\7y\2\2\u0173\u0174\7k\2\2\u0174\u0175\7v\2\2\u0175")
        buf.write("\u0176\7e\2\2\u0176\u0177\7j\2\2\u0177~\3\2\2\2\u0178")
        buf.write("\u0179\7e\2\2\u0179\u017a\7c\2\2\u017a\u017b\7u\2\2\u017b")
        buf.write("\u017c\7g\2\2\u017c\u0080\3\2\2\2\u017d\u017e\7f\2\2\u017e")
        buf.write("\u017f\7g\2\2\u017f\u0180\7h\2\2\u0180\u0181\7c\2\2\u0181")
        buf.write("\u0182\7w\2\2\u0182\u0183\7n\2\2\u0183\u0184\7v\2\2\u0184")
        buf.write("\u0082\3\2\2\2\u0185\u0186\7y\2\2\u0186\u0187\7j\2\2\u0187")
        buf.write("\u0188\7k\2\2\u0188\u0189\7n\2\2\u0189\u018a\7g\2\2\u018a")
        buf.write("\u0084\3\2\2\2\u018b\u018c\7f\2\2\u018c\u018d\7q\2\2\u018d")
        buf.write("\u0086\3\2\2\2\u018e\u018f\7h\2\2\u018f\u0190\7q\2\2\u0190")
        buf.write("\u0191\7t\2\2\u0191\u0088\3\2\2\2\u0192\u0193\7t\2\2\u0193")
        buf.write("\u0194\7g\2\2\u0194\u0195\7v\2\2\u0195\u0196\7w\2\2\u0196")
        buf.write("\u0197\7t\2\2\u0197\u0198\7p\2\2\u0198\u008a\3\2\2\2\u0199")
        buf.write("\u019a\7d\2\2\u019a\u019b\7t\2\2\u019b\u019c\7g\2\2\u019c")
        buf.write("\u019d\7c\2\2\u019d\u019e\7m\2\2\u019e\u008c\3\2\2\2\u019f")
        buf.write("\u01a0\7e\2\2\u01a0\u01a1\7q\2\2\u01a1\u01a2\7p\2\2\u01a2")
        buf.write("\u01a3\7v\2\2\u01a3\u01a4\7k\2\2\u01a4\u01a5\7p\2\2\u01a5")
        buf.write("\u01a6\7w\2\2\u01a6\u01a7\7g\2\2\u01a7\u008e\3\2\2\2\u01a8")
        buf.write("\u01a9\7i\2\2\u01a9\u01aa\7q\2\2\u01aa\u01ab\7v\2\2\u01ab")
        buf.write("\u01ac\7q\2\2\u01ac\u0090\3\2\2\2\u01ad\u01ae\7v\2\2\u01ae")
        buf.write("\u01af\7{\2\2\u01af\u01b0\7r\2\2\u01b0\u01b1\7g\2\2\u01b1")
        buf.write("\u01b2\7f\2\2\u01b2\u01b3\7g\2\2\u01b3\u01b4\7h\2\2\u01b4")
        buf.write("\u0092\3\2\2\2\u01b5\u01b6\7k\2\2\u01b6\u01b7\7o\2\2\u01b7")
        buf.write("\u01b8\7r\2\2\u01b8\u01b9\7q\2\2\u01b9\u01ba\7t\2\2\u01ba")
        buf.write("\u01bb\7v\2\2\u01bb\u0094\3\2\2\2\u01bc\u01bd\7u\2\2\u01bd")
        buf.write("\u01be\7k\2\2\u01be\u01bf\7|\2\2\u01bf\u01c0\7g\2\2\u01c0")
        buf.write("\u01c1\7q\2\2\u01c1\u01c2\7h\2\2\u01c2\u0096\3\2\2\2\u01c3")
        buf.write("\u01c7\t\2\2\2\u01c4\u01c6\t\3\2\2\u01c5\u01c4\3\2\2\2")
        buf.write("\u01c6\u01c9\3\2\2\2\u01c7\u01c5\3\2\2\2\u01c7\u01c8\3")
        buf.write("\2\2\2\u01c8\u0098\3\2\2\2\u01c9\u01c7\3\2\2\2\u01ca\u01ce")
        buf.write("\t\4\2\2\u01cb\u01cd\t\5\2\2\u01cc\u01cb\3\2\2\2\u01cd")
        buf.write("\u01d0\3\2\2\2\u01ce\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2")
        buf.write("\u01cf\u01d2\3\2\2\2\u01d0\u01ce\3\2\2\2\u01d1\u01d3\7")
        buf.write("W\2\2\u01d2\u01d1\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3\u01d5")
        buf.write("\3\2\2\2\u01d4\u01d6\7N\2\2\u01d5\u01d4\3\2\2\2\u01d5")
        buf.write("\u01d6\3\2\2\2\u01d6\u01f2\3\2\2\2\u01d7\u01d8\7\62\2")
        buf.write("\2\u01d8\u01da\t\6\2\2\u01d9\u01db\t\7\2\2\u01da\u01d9")
        buf.write("\3\2\2\2\u01db\u01dc\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc")
        buf.write("\u01dd\3\2\2\2\u01dd\u01df\3\2\2\2\u01de\u01e0\7W\2\2")
        buf.write("\u01df\u01de\3\2\2\2\u01df\u01e0\3\2\2\2\u01e0\u01e2\3")
        buf.write("\2\2\2\u01e1\u01e3\7N\2\2\u01e2\u01e1\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01f2\3\2\2\2\u01e4\u01e8\7\62\2\2\u01e5")
        buf.write("\u01e7\t\b\2\2\u01e6\u01e5\3\2\2\2\u01e7\u01ea\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ec\3")
        buf.write("\2\2\2\u01ea\u01e8\3\2\2\2\u01eb\u01ed\7W\2\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ec\u01ed\3\2\2\2\u01ed\u01ef\3\2\2\2\u01ee")
        buf.write("\u01f0\7N\2\2\u01ef\u01ee\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f2\3\2\2\2\u01f1\u01ca\3\2\2\2\u01f1\u01d7\3")
        buf.write("\2\2\2\u01f1\u01e4\3\2\2\2\u01f2\u009a\3\2\2\2\u01f3\u01f5")
        buf.write("\t\t\2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6")
        buf.write("\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u01f8\3\2\2\2")
        buf.write("\u01f8\u01f9\bN\2\2\u01f9\u009c\3\2\2\2\u01fa\u01fb\7")
        buf.write("\61\2\2\u01fb\u01fc\7\61\2\2\u01fc\u0200\3\2\2\2\u01fd")
        buf.write("\u01ff\n\n\2\2\u01fe\u01fd\3\2\2\2\u01ff\u0202\3\2\2\2")
        buf.write("\u0200\u01fe\3\2\2\2\u0200\u0201\3\2\2\2\u0201\u0207\3")
        buf.write("\2\2\2\u0202\u0200\3\2\2\2\u0203\u0208\7\f\2\2\u0204\u0205")
        buf.write("\7\17\2\2\u0205\u0208\7\f\2\2\u0206\u0208\7\17\2\2\u0207")
        buf.write("\u0203\3\2\2\2\u0207\u0204\3\2\2\2\u0207\u0206\3\2\2\2")
        buf.write("\u0207\u0208\3\2\2\2\u0208\u009e\3\2\2\2\u0209\u020a\7")
        buf.write("\61\2\2\u020a\u020b\7,\2\2\u020b\u020f\3\2\2\2\u020c\u020e")
        buf.write("\13\2\2\2\u020d\u020c\3\2\2\2\u020e\u0211\3\2\2\2\u020f")
        buf.write("\u0210\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0212\3\2\2\2")
        buf.write("\u0211\u020f\3\2\2\2\u0212\u0213\7,\2\2\u0213\u0214\7")
        buf.write("\61\2\2\u0214\u00a0\3\2\2\2\u0215\u021b\7$\2\2\u0216\u0217")
        buf.write("\7^\2\2\u0217\u021a\7$\2\2\u0218\u021a\13\2\2\2\u0219")
        buf.write("\u0216\3\2\2\2\u0219\u0218\3\2\2\2\u021a\u021d\3\2\2\2")
        buf.write("\u021b\u021c\3\2\2\2\u021b\u0219\3\2\2\2\u021c\u021e\3")
        buf.write("\2\2\2\u021d\u021b\3\2\2\2\u021e\u021f\7$\2\2\u021f\u00a2")
        buf.write("\3\2\2\2\u0220\u0224\7)\2\2\u0221\u0222\7^\2\2\u0222\u0225")
        buf.write("\13\2\2\2\u0223\u0225\n\13\2\2\u0224\u0221\3\2\2\2\u0224")
        buf.write("\u0223\3\2\2\2\u0225\u0226\3\2\2\2\u0226\u0227\7)\2\2")
        buf.write("\u0227\u00a4\3\2\2\2\25\2\u01c7\u01ce\u01d2\u01d5\u01dc")
        buf.write("\u01df\u01e2\u01e8\u01ec\u01ef\u01f1\u01f6\u0200\u0207")
        buf.write("\u020f\u0219\u021b\u0224\3\b\2\2")
        return buf.getvalue()


class CprestoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    VOID = 47
    CHAR = 48
    SHORT = 49
    INT = 50
    LONG = 51
    STRUCT = 52
    UNION = 53
    ENUM = 54
    STATIC = 55
    EXTERN = 56
    CONST = 57
    SIGNED = 58
    UNSIGNED = 59
    IF = 60
    ELSE = 61
    SWITCH = 62
    CASE = 63
    DEFAULT = 64
    WHILE = 65
    DO = 66
    FOR = 67
    RETURN = 68
    BREAK = 69
    CONTINUE = 70
    GOTO = 71
    TYPEDEF = 72
    IMPORT = 73
    SIZEOF = 74
    IDENTIFIER = 75
    INTEGER = 76
    SPACES = 77
    LINE_COMMENT = 78
    BLOCK_COMMENT = 79
    STRING = 80
    CHARACTER = 81

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "';'", "'('", "')'", "'='", "','", "'...'", "'{'", "'}'", 
            "'['", "']'", "'*'", "':'", "'+='", "'-='", "'*='", "'/='", 
            "'%='", "'&='", "'|='", "'^='", "'<<='", "'>>='", "'?'", "'||'", 
            "'&&'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", "'|'", 
            "'^'", "'&'", "'>>'", "'<<'", "'+'", "'-'", "'/'", "'%'", "'++'", 
            "'--'", "'!'", "'~'", "'->'", "'void'", "'char'", "'short'", 
            "'int'", "'long'", "'struct'", "'union'", "'enum'", "'static'", 
            "'extern'", "'const'", "'signed'", "'unsigned'", "'if'", "'else'", 
            "'switch'", "'case'", "'default'", "'while'", "'do'", "'for'", 
            "'return'", "'break'", "'continue'", "'goto'", "'typedef'", 
            "'import'", "'sizeof'" ]

    symbolicNames = [ "<INVALID>",
            "VOID", "CHAR", "SHORT", "INT", "LONG", "STRUCT", "UNION", "ENUM", 
            "STATIC", "EXTERN", "CONST", "SIGNED", "UNSIGNED", "IF", "ELSE", 
            "SWITCH", "CASE", "DEFAULT", "WHILE", "DO", "FOR", "RETURN", 
            "BREAK", "CONTINUE", "GOTO", "TYPEDEF", "IMPORT", "SIZEOF", 
            "IDENTIFIER", "INTEGER", "SPACES", "LINE_COMMENT", "BLOCK_COMMENT", 
            "STRING", "CHARACTER" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "VOID", "CHAR", "SHORT", "INT", "LONG", 
                  "STRUCT", "UNION", "ENUM", "STATIC", "EXTERN", "CONST", 
                  "SIGNED", "UNSIGNED", "IF", "ELSE", "SWITCH", "CASE", 
                  "DEFAULT", "WHILE", "DO", "FOR", "RETURN", "BREAK", "CONTINUE", 
                  "GOTO", "TYPEDEF", "IMPORT", "SIZEOF", "IDENTIFIER", "INTEGER", 
                  "SPACES", "LINE_COMMENT", "BLOCK_COMMENT", "STRING", "CHARACTER" ]

    grammarFileName = "Cpresto.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


