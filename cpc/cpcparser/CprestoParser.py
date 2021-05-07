# Generated from Cpresto.g4 by ANTLR 4.9
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


import sys
sys.path.append('../')
from type.IntegerTypeRef import IntegerTypeRef
from exception.CompileException import CompileException

from abst.AbstractAssignNode import *
from abst.AddressNode import *
from abst.ArefNode import *
from abst.AssignNode import *
from abst.AST import *
#from abst.ASTVisitor import *
from abst.BinaryOpNode import *
from abst.BlockNode import *
from abst.BreakNode import *
from abst.CaseNode import *
from abst.CastNode import *
from abst.CprestoToken import *
from abst.CompositeTypeDefinition import *
from abst.CondExprNode import *
from abst.ContinueNode import *
from abst.Declarations import *
#from abst.DeclarationVisitor import *
from abst.DereferenceNode import *
from abst.DoWhileNode import *
from abst.Dumpable import *
from abst.Dumper import *
from abst.ExprNode import *
from abst.ExprStmtNode import *
from abst.ForNode import *
from abst.FuncallNode import *
from abst.GotoNode import *
from abst.IfNode import *
from abst.IntegerLiteralNode import *
from abst.LabelNode import *
from abst.LHSNode import *
from abst.LiteralNode import *
from abst.Location import *
from abst.LogicalAndNode import *
from abst.LogicalOrNode import *
from abst.MemberNode import *
from abst.Node import *
from abst.OpAssignNode import *
from abst.PrefixOpNode import *
from abst.PtrMemberNode import *
from abst.ReturnNode import *
from abst.SizeofExprNode import *
from abst.SizeofTypeNode import *
from abst.Slot import *
from abst.StmtNode import *
from abst.StringLiteralNode import *
from abst.StructNode import *
from abst.SuffixOpNode import *
from abst.SwitchNode import *
from abst.TypeDefinition import *
from abst.TypedefNode import *
from abst.TypeNode import *
from abst.UnaryArithmeticOpNode import *
from abst.UnaryOpNode import *
from abst.UnionNode import *
from abst.VariableNode import *
from abst.WhileNode import *

from entity.Constant import *
from entity.ConstantEntry import *
from entity.ConstantTable import *
from entity.DefinedFunction import *
from entity.DefinedVariable import *
from entity.Entity import *
#from entity.EntityVisitor import *
from entity.Function import *
from entity.LocalScope import *
from entity.Parameter import *
from entity.Params import *
from entity.ParamSlots import *
from entity.Scope import *
from entity.TopLevelScope import *
from entity.UndefinedFunction import *
from entity.UndefinedVariable import *
from entity.Variable import *

from type.ArrayType import *
from type.ArrayTypeRef import *
from type.CompositeType import *
from type.FunctionType import *
from type.FunctionTypeRef import *
from type.IntegerType import *
from type.IntegerTypeRef import *
from type.NamedType import *
from type.ParamTypeRefs import *
from type.ParamTypes import *
from type.PointerType import *
from type.PointerTypeRef import *
from type.StructType import *
from type.StructTypeRef import *
from type.Type import *
from type.TypeRef import *
from type.TypeTable import *
from type.UnionType import *
from type.UnionTypeRef import *
from type.UserType import *
from type.UserTypeRef import *
from type.VoidType import *
from type.VoidTypeRef import *

from asm.Label import Label
from utils.ErrorHandler import ErrorHandler

from exception.CompileException import *
from exception.FileException import *
from exception.IPCException import *
from exception.JumpError import *
from exception.OptionParseError import *
from exception.SemanticError import *
from exception.SemanticException import *
from exception.SyntaxException import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3S")
        buf.write("\u039c\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\3\2\3\2\7\2\u0080\n\2\f\2\16\2")
        buf.write("\u0083\13\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\u008e")
        buf.write("\n\3\f\3\16\3\u0091\13\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\7\7\u00ba\n\7\f\7\16\7\u00bd\13\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00c8\n\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\5\b\u00d1\n\b\3\b\3\b\7\b\u00d5")
        buf.write("\n\b\f\b\16\b\u00d8\13\b\3\b\3\b\3\b\3\t\5\t\u00de\n\t")
        buf.write("\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\13\5\13\u00f1\n\13\3\13\3\13\5\13\u00f5")
        buf.write("\n\13\3\f\3\f\3\f\3\f\3\f\3\f\7\f\u00fd\n\f\f\f\16\f\u0100")
        buf.write("\13\f\3\f\3\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\7\17\u0111\n\17\f\17\16\17\u0114")
        buf.write("\13\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write("\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\7\23\u0131\n\23\f")
        buf.write("\23\16\23\u0134\13\23\3\23\3\23\3\23\3\24\3\24\3\24\3")
        buf.write("\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\7\27\u0155\n\27\f\27\16\27\u0158\13\27")
        buf.write("\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u0162\n")
        buf.write("\30\3\30\3\30\5\30\u0166\n\30\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\7\31\u016e\n\31\f\31\16\31\u0171\13\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u0194")
        buf.write("\n\32\3\33\3\33\3\33\7\33\u0199\n\33\f\33\16\33\u019c")
        buf.write("\13\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u01c7\n\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\3\36\5\36\u01d5\n\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\5!\u01ec\n!\3!\3!\5!\u01f0\n!\3!\3!\5!\u01f4\n")
        buf.write("!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3")
        buf.write("#\3#\7#\u0206\n#\f#\16#\u0209\13#\3#\3#\3#\5#\u020e\n")
        buf.write("#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\6%\u021b\n%\r%\16%")
        buf.write("\u021c\3%\3%\3&\3&\3&\3&\3&\3\'\3\'\3\'\6\'\u0229\n\'")
        buf.write("\r\'\16\'\u022a\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*")
        buf.write("\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\5+\u0244\n+\3,\3,\3")
        buf.write(",\3,\3,\3,\3,\3,\3,\3,\3,\3,\3,\5,\u0253\n,\3-\3-\3-\3")
        buf.write("-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\5-\u0269")
        buf.write("\n-\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0273\n.\3/\3/\3/\3/\3")
        buf.write("/\7/\u027a\n/\f/\16/\u027d\13/\3/\3/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\7\60\u0286\n\60\f\60\16\60\u0289\13\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61")
        buf.write("\3\61\3\61\3\61\3\61\7\61\u02a6\n\61\f\61\16\61\u02a9")
        buf.write("\13\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\7\62\u02b2\n")
        buf.write("\62\f\62\16\62\u02b5\13\62\3\62\3\62\3\63\3\63\3\63\3")
        buf.write("\63\3\63\7\63\u02be\n\63\f\63\16\63\u02c1\13\63\3\63\3")
        buf.write("\63\3\64\3\64\3\64\3\64\3\64\7\64\u02ca\n\64\f\64\16\64")
        buf.write("\u02cd\13\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3")
        buf.write("\65\3\65\3\65\7\65\u02da\n\65\f\65\16\65\u02dd\13\65\3")
        buf.write("\65\3\65\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66\3\66")
        buf.write("\7\66\u02ea\n\66\f\66\16\66\u02ed\13\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\7\67\u02fe\n\67\f\67\16\67\u0301\13\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\38\38\38\58\u030e\n8\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write("9\39\39\39\39\59\u033d\n9\3:\3:\3:\3:\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\7:\u0357\n")
        buf.write(":\f:\16:\u035a\13:\3:\3:\3;\3;\3;\3;\3;\3;\7;\u0364\n")
        buf.write(";\f;\16;\u0367\13;\5;\u0369\n;\3;\3;\3<\3<\3<\3<\3<\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\5<\u037a\n<\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\7>\u0395\n>\f>\16>\u0398\13>\3>\3>\3>\2\2?\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\2\2\u03d2\2\u0081\3")
        buf.write("\2\2\2\4\u0086\3\2\2\2\6\u0095\3\2\2\2\b\u009e\3\2\2\2")
        buf.write("\n\u00a4\3\2\2\2\f\u00bb\3\2\2\2\16\u00c0\3\2\2\2\20\u00dd")
        buf.write("\3\2\2\2\22\u00e1\3\2\2\2\24\u00f4\3\2\2\2\26\u00f6\3")
        buf.write("\2\2\2\30\u0103\3\2\2\2\32\u0107\3\2\2\2\34\u0112\3\2")
        buf.write("\2\2\36\u0117\3\2\2\2 \u011f\3\2\2\2\"\u0125\3\2\2\2$")
        buf.write("\u012b\3\2\2\2&\u0138\3\2\2\2(\u013c\3\2\2\2*\u0142\3")
        buf.write("\2\2\2,\u0145\3\2\2\2.\u0165\3\2\2\2\60\u0167\3\2\2\2")
        buf.write("\62\u0193\3\2\2\2\64\u019a\3\2\2\2\66\u01c6\3\2\2\28\u01c8")
        buf.write("\3\2\2\2:\u01cd\3\2\2\2<\u01d8\3\2\2\2>\u01df\3\2\2\2")
        buf.write("@\u01e8\3\2\2\2B\u01f9\3\2\2\2D\u0207\3\2\2\2F\u0211\3")
        buf.write("\2\2\2H\u021a\3\2\2\2J\u0220\3\2\2\2L\u0228\3\2\2\2N\u022e")
        buf.write("\3\2\2\2P\u0232\3\2\2\2R\u0236\3\2\2\2T\u0243\3\2\2\2")
        buf.write("V\u0252\3\2\2\2X\u0268\3\2\2\2Z\u026a\3\2\2\2\\\u0274")
        buf.write("\3\2\2\2^\u0280\3\2\2\2`\u028c\3\2\2\2b\u02ac\3\2\2\2")
        buf.write("d\u02b8\3\2\2\2f\u02c4\3\2\2\2h\u02d0\3\2\2\2j\u02e0\3")
        buf.write("\2\2\2l\u02f0\3\2\2\2n\u030d\3\2\2\2p\u033c\3\2\2\2r\u033e")
        buf.write("\3\2\2\2t\u0368\3\2\2\2v\u0379\3\2\2\2x\u037b\3\2\2\2")
        buf.write("z\u0380\3\2\2\2|}\5\4\3\2}~\b\2\1\2~\u0080\3\2\2\2\177")
        buf.write("|\3\2\2\2\u0080\u0083\3\2\2\2\u0081\177\3\2\2\2\u0081")
        buf.write("\u0082\3\2\2\2\u0082\u0084\3\2\2\2\u0083\u0081\3\2\2\2")
        buf.write("\u0084\u0085\b\2\1\2\u0085\3\3\2\2\2\u0086\u0087\7K\2")
        buf.write("\2\u0087\u0088\5\n\6\2\u0088\u008f\b\3\1\2\u0089\u008a")
        buf.write("\7\3\2\2\u008a\u008b\5\n\6\2\u008b\u008c\b\3\1\2\u008c")
        buf.write("\u008e\3\2\2\2\u008d\u0089\3\2\2\2\u008e\u0091\3\2\2\2")
        buf.write("\u008f\u008d\3\2\2\2\u008f\u0090\3\2\2\2\u0090\u0092\3")
        buf.write("\2\2\2\u0091\u008f\3\2\2\2\u0092\u0093\7\4\2\2\u0093\u0094")
        buf.write("\b\3\1\2\u0094\5\3\2\2\2\u0095\u0096\7:\2\2\u0096\u0097")
        buf.write("\5,\27\2\u0097\u0098\5\n\6\2\u0098\u0099\7\5\2\2\u0099")
        buf.write("\u009a\5\24\13\2\u009a\u009b\7\6\2\2\u009b\u009c\7\4\2")
        buf.write("\2\u009c\u009d\b\4\1\2\u009d\7\3\2\2\2\u009e\u009f\7:")
        buf.write("\2\2\u009f\u00a0\5*\26\2\u00a0\u00a1\5\n\6\2\u00a1\u00a2")
        buf.write("\7\4\2\2\u00a2\u00a3\b\5\1\2\u00a3\t\3\2\2\2\u00a4\u00a5")
        buf.write("\7M\2\2\u00a5\u00a6\b\6\1\2\u00a6\13\3\2\2\2\u00a7\u00a8")
        buf.write("\5\22\n\2\u00a8\u00a9\b\7\1\2\u00a9\u00ba\3\2\2\2\u00aa")
        buf.write("\u00ab\5\16\b\2\u00ab\u00ac\b\7\1\2\u00ac\u00ba\3\2\2")
        buf.write("\2\u00ad\u00ae\5\36\20\2\u00ae\u00af\b\7\1\2\u00af\u00ba")
        buf.write("\3\2\2\2\u00b0\u00b1\5 \21\2\u00b1\u00b2\b\7\1\2\u00b2")
        buf.write("\u00ba\3\2\2\2\u00b3\u00b4\5\"\22\2\u00b4\u00b5\b\7\1")
        buf.write("\2\u00b5\u00ba\3\2\2\2\u00b6\u00b7\5(\25\2\u00b7\u00b8")
        buf.write("\b\7\1\2\u00b8\u00ba\3\2\2\2\u00b9\u00a7\3\2\2\2\u00b9")
        buf.write("\u00aa\3\2\2\2\u00b9\u00ad\3\2\2\2\u00b9\u00b0\3\2\2\2")
        buf.write("\u00b9\u00b3\3\2\2\2\u00b9\u00b6\3\2\2\2\u00ba\u00bd\3")
        buf.write("\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00be")
        buf.write("\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00bf\b\7\1\2\u00bf")
        buf.write("\r\3\2\2\2\u00c0\u00c1\5\20\t\2\u00c1\u00c2\5*\26\2\u00c2")
        buf.write("\u00c7\5\n\6\2\u00c3\u00c4\7\7\2\2\u00c4\u00c5\5V,\2\u00c5")
        buf.write("\u00c6\b\b\1\2\u00c6\u00c8\3\2\2\2\u00c7\u00c3\3\2\2\2")
        buf.write("\u00c7\u00c8\3\2\2\2\u00c8\u00c9\3\2\2\2\u00c9\u00d6\b")
        buf.write("\b\1\2\u00ca\u00cb\7\b\2\2\u00cb\u00d0\5\n\6\2\u00cc\u00cd")
        buf.write("\7\7\2\2\u00cd\u00ce\5V,\2\u00ce\u00cf\b\b\1\2\u00cf\u00d1")
        buf.write("\3\2\2\2\u00d0\u00cc\3\2\2\2\u00d0\u00d1\3\2\2\2\u00d1")
        buf.write("\u00d2\3\2\2\2\u00d2\u00d3\b\b\1\2\u00d3\u00d5\3\2\2\2")
        buf.write("\u00d4\u00ca\3\2\2\2\u00d5\u00d8\3\2\2\2\u00d6\u00d4\3")
        buf.write("\2\2\2\u00d6\u00d7\3\2\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00d6")
        buf.write("\3\2\2\2\u00d9\u00da\7\4\2\2\u00da\u00db\b\b\1\2\u00db")
        buf.write("\17\3\2\2\2\u00dc\u00de\79\2\2\u00dd\u00dc\3\2\2\2\u00dd")
        buf.write("\u00de\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00e0\b\t\1\2")
        buf.write("\u00e0\21\3\2\2\2\u00e1\u00e2\5\20\t\2\u00e2\u00e3\5,")
        buf.write("\27\2\u00e3\u00e4\5\n\6\2\u00e4\u00e5\7\5\2\2\u00e5\u00e6")
        buf.write("\5\24\13\2\u00e6\u00e7\7\6\2\2\u00e7\u00e8\5\32\16\2\u00e8")
        buf.write("\u00e9\b\n\1\2\u00e9\23\3\2\2\2\u00ea\u00eb\7\61\2\2\u00eb")
        buf.write("\u00f5\b\13\1\2\u00ec\u00f0\5\26\f\2\u00ed\u00ee\7\b\2")
        buf.write("\2\u00ee\u00ef\7\t\2\2\u00ef\u00f1\b\13\1\2\u00f0\u00ed")
        buf.write("\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write("\u00f3\b\13\1\2\u00f3\u00f5\3\2\2\2\u00f4\u00ea\3\2\2")
        buf.write("\2\u00f4\u00ec\3\2\2\2\u00f5\25\3\2\2\2\u00f6\u00f7\5")
        buf.write("\30\r\2\u00f7\u00fe\b\f\1\2\u00f8\u00f9\7\b\2\2\u00f9")
        buf.write("\u00fa\5\30\r\2\u00fa\u00fb\b\f\1\2\u00fb\u00fd\3\2\2")
        buf.write("\2\u00fc\u00f8\3\2\2\2\u00fd\u0100\3\2\2\2\u00fe\u00fc")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0101\3\2\2\2\u0100")
        buf.write("\u00fe\3\2\2\2\u0101\u0102\b\f\1\2\u0102\27\3\2\2\2\u0103")
        buf.write("\u0104\5*\26\2\u0104\u0105\5\n\6\2\u0105\u0106\b\r\1\2")
        buf.write("\u0106\31\3\2\2\2\u0107\u0108\7\n\2\2\u0108\u0109\5\34")
        buf.write("\17\2\u0109\u010a\5\64\33\2\u010a\u010b\7\13\2\2\u010b")
        buf.write("\u010c\b\16\1\2\u010c\33\3\2\2\2\u010d\u010e\5\16\b\2")
        buf.write("\u010e\u010f\b\17\1\2\u010f\u0111\3\2\2\2\u0110\u010d")
        buf.write("\3\2\2\2\u0111\u0114\3\2\2\2\u0112\u0110\3\2\2\2\u0112")
        buf.write("\u0113\3\2\2\2\u0113\u0115\3\2\2\2\u0114\u0112\3\2\2\2")
        buf.write("\u0115\u0116\b\17\1\2\u0116\35\3\2\2\2\u0117\u0118\7;")
        buf.write("\2\2\u0118\u0119\5*\26\2\u0119\u011a\5\n\6\2\u011a\u011b")
        buf.write("\7\7\2\2\u011b\u011c\5V,\2\u011c\u011d\7\4\2\2\u011d\u011e")
        buf.write("\b\20\1\2\u011e\37\3\2\2\2\u011f\u0120\7\66\2\2\u0120")
        buf.write("\u0121\5\n\6\2\u0121\u0122\5$\23\2\u0122\u0123\7\4\2\2")
        buf.write("\u0123\u0124\b\21\1\2\u0124!\3\2\2\2\u0125\u0126\7\67")
        buf.write("\2\2\u0126\u0127\5\n\6\2\u0127\u0128\5$\23\2\u0128\u0129")
        buf.write("\7\4\2\2\u0129\u012a\b\22\1\2\u012a#\3\2\2\2\u012b\u0132")
        buf.write("\7\n\2\2\u012c\u012d\5&\24\2\u012d\u012e\7\4\2\2\u012e")
        buf.write("\u012f\b\23\1\2\u012f\u0131\3\2\2\2\u0130\u012c\3\2\2")
        buf.write("\2\u0131\u0134\3\2\2\2\u0132\u0130\3\2\2\2\u0132\u0133")
        buf.write("\3\2\2\2\u0133\u0135\3\2\2\2\u0134\u0132\3\2\2\2\u0135")
        buf.write("\u0136\7\13\2\2\u0136\u0137\b\23\1\2\u0137%\3\2\2\2\u0138")
        buf.write("\u0139\5*\26\2\u0139\u013a\5\n\6\2\u013a\u013b\b\24\1")
        buf.write("\2\u013b\'\3\2\2\2\u013c\u013d\7J\2\2\u013d\u013e\5,\27")
        buf.write("\2\u013e\u013f\7M\2\2\u013f\u0140\7\4\2\2\u0140\u0141")
        buf.write("\b\25\1\2\u0141)\3\2\2\2\u0142\u0143\5,\27\2\u0143\u0144")
        buf.write("\b\26\1\2\u0144+\3\2\2\2\u0145\u0156\5\62\32\2\u0146\u0147")
        buf.write("\7\f\2\2\u0147\u0148\7\r\2\2\u0148\u0155\b\27\1\2\u0149")
        buf.write("\u014a\7\f\2\2\u014a\u014b\7N\2\2\u014b\u014c\7\r\2\2")
        buf.write("\u014c\u0155\b\27\1\2\u014d\u014e\7\16\2\2\u014e\u0155")
        buf.write("\b\27\1\2\u014f\u0150\7\5\2\2\u0150\u0151\5.\30\2\u0151")
        buf.write("\u0152\7\6\2\2\u0152\u0153\b\27\1\2\u0153\u0155\3\2\2")
        buf.write("\2\u0154\u0146\3\2\2\2\u0154\u0149\3\2\2\2\u0154\u014d")
        buf.write("\3\2\2\2\u0154\u014f\3\2\2\2\u0155\u0158\3\2\2\2\u0156")
        buf.write("\u0154\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0159\3\2\2\2")
        buf.write("\u0158\u0156\3\2\2\2\u0159\u015a\b\27\1\2\u015a-\3\2\2")
        buf.write("\2\u015b\u015c\7\61\2\2\u015c\u0166\b\30\1\2\u015d\u0161")
        buf.write("\5\60\31\2\u015e\u015f\7\b\2\2\u015f\u0160\7\t\2\2\u0160")
        buf.write("\u0162\b\30\1\2\u0161\u015e\3\2\2\2\u0161\u0162\3\2\2")
        buf.write("\2\u0162\u0163\3\2\2\2\u0163\u0164\b\30\1\2\u0164\u0166")
        buf.write("\3\2\2\2\u0165\u015b\3\2\2\2\u0165\u015d\3\2\2\2\u0166")
        buf.write("/\3\2\2\2\u0167\u0168\5,\27\2\u0168\u016f\b\31\1\2\u0169")
        buf.write("\u016a\7\b\2\2\u016a\u016b\5,\27\2\u016b\u016c\b\31\1")
        buf.write("\2\u016c\u016e\3\2\2\2\u016d\u0169\3\2\2\2\u016e\u0171")
        buf.write("\3\2\2\2\u016f\u016d\3\2\2\2\u016f\u0170\3\2\2\2\u0170")
        buf.write("\u0172\3\2\2\2\u0171\u016f\3\2\2\2\u0172\u0173\b\31\1")
        buf.write("\2\u0173\61\3\2\2\2\u0174\u0175\7\61\2\2\u0175\u0194\b")
        buf.write("\32\1\2\u0176\u0177\7\62\2\2\u0177\u0194\b\32\1\2\u0178")
        buf.write("\u0179\7\63\2\2\u0179\u0194\b\32\1\2\u017a\u017b\7\64")
        buf.write("\2\2\u017b\u0194\b\32\1\2\u017c\u017d\7\65\2\2\u017d\u0194")
        buf.write("\b\32\1\2\u017e\u017f\7=\2\2\u017f\u0180\7\62\2\2\u0180")
        buf.write("\u0194\b\32\1\2\u0181\u0182\7=\2\2\u0182\u0183\7\63\2")
        buf.write("\2\u0183\u0194\b\32\1\2\u0184\u0185\7=\2\2\u0185\u0186")
        buf.write("\7\64\2\2\u0186\u0194\b\32\1\2\u0187\u0188\7=\2\2\u0188")
        buf.write("\u0189\7\65\2\2\u0189\u0194\b\32\1\2\u018a\u018b\7\66")
        buf.write("\2\2\u018b\u018c\7M\2\2\u018c\u0194\b\32\1\2\u018d\u018e")
        buf.write("\7\67\2\2\u018e\u018f\7M\2\2\u018f\u0194\b\32\1\2\u0190")
        buf.write("\u0191\6\32\2\2\u0191\u0192\7M\2\2\u0192\u0194\b\32\1")
        buf.write("\2\u0193\u0174\3\2\2\2\u0193\u0176\3\2\2\2\u0193\u0178")
        buf.write("\3\2\2\2\u0193\u017a\3\2\2\2\u0193\u017c\3\2\2\2\u0193")
        buf.write("\u017e\3\2\2\2\u0193\u0181\3\2\2\2\u0193\u0184\3\2\2\2")
        buf.write("\u0193\u0187\3\2\2\2\u0193\u018a\3\2\2\2\u0193\u018d\3")
        buf.write("\2\2\2\u0193\u0190\3\2\2\2\u0194\63\3\2\2\2\u0195\u0196")
        buf.write("\5\66\34\2\u0196\u0197\b\33\1\2\u0197\u0199\3\2\2\2\u0198")
        buf.write("\u0195\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2")
        buf.write("\u019a\u019b\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019a\3")
        buf.write("\2\2\2\u019d\u019e\b\33\1\2\u019e\65\3\2\2\2\u019f\u01a0")
        buf.write("\7\4\2\2\u01a0\u01c7\b\34\1\2\u01a1\u01a2\58\35\2\u01a2")
        buf.write("\u01a3\b\34\1\2\u01a3\u01c7\3\2\2\2\u01a4\u01a5\5V,\2")
        buf.write("\u01a5\u01a6\7\4\2\2\u01a6\u01a7\b\34\1\2\u01a7\u01c7")
        buf.write("\3\2\2\2\u01a8\u01a9\5\32\16\2\u01a9\u01aa\b\34\1\2\u01aa")
        buf.write("\u01c7\3\2\2\2\u01ab\u01ac\5:\36\2\u01ac\u01ad\b\34\1")
        buf.write("\2\u01ad\u01c7\3\2\2\2\u01ae\u01af\5<\37\2\u01af\u01b0")
        buf.write("\b\34\1\2\u01b0\u01c7\3\2\2\2\u01b1\u01b2\5> \2\u01b2")
        buf.write("\u01b3\b\34\1\2\u01b3\u01c7\3\2\2\2\u01b4\u01b5\5@!\2")
        buf.write("\u01b5\u01b6\b\34\1\2\u01b6\u01c7\3\2\2\2\u01b7\u01b8")
        buf.write("\5B\"\2\u01b8\u01b9\b\34\1\2\u01b9\u01c7\3\2\2\2\u01ba")
        buf.write("\u01bb\5N(\2\u01bb\u01bc\b\34\1\2\u01bc\u01c7\3\2\2\2")
        buf.write("\u01bd\u01be\5P)\2\u01be\u01bf\b\34\1\2\u01bf\u01c7\3")
        buf.write("\2\2\2\u01c0\u01c1\5R*\2\u01c1\u01c2\b\34\1\2\u01c2\u01c7")
        buf.write("\3\2\2\2\u01c3\u01c4\5T+\2\u01c4\u01c5\b\34\1\2\u01c5")
        buf.write("\u01c7\3\2\2\2\u01c6\u019f\3\2\2\2\u01c6\u01a1\3\2\2\2")
        buf.write("\u01c6\u01a4\3\2\2\2\u01c6\u01a8\3\2\2\2\u01c6\u01ab\3")
        buf.write("\2\2\2\u01c6\u01ae\3\2\2\2\u01c6\u01b1\3\2\2\2\u01c6\u01b4")
        buf.write("\3\2\2\2\u01c6\u01b7\3\2\2\2\u01c6\u01ba\3\2\2\2\u01c6")
        buf.write("\u01bd\3\2\2\2\u01c6\u01c0\3\2\2\2\u01c6\u01c3\3\2\2\2")
        buf.write("\u01c7\67\3\2\2\2\u01c8\u01c9\7M\2\2\u01c9\u01ca\7\17")
        buf.write("\2\2\u01ca\u01cb\5\66\34\2\u01cb\u01cc\b\35\1\2\u01cc")
        buf.write("9\3\2\2\2\u01cd\u01ce\7>\2\2\u01ce\u01cf\7\5\2\2\u01cf")
        buf.write("\u01d0\5V,\2\u01d0\u01d1\7\6\2\2\u01d1\u01d4\5\66\34\2")
        buf.write("\u01d2\u01d3\7?\2\2\u01d3\u01d5\5\66\34\2\u01d4\u01d2")
        buf.write("\3\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6")
        buf.write("\u01d7\b\36\1\2\u01d7;\3\2\2\2\u01d8\u01d9\7C\2\2\u01d9")
        buf.write("\u01da\7\5\2\2\u01da\u01db\5V,\2\u01db\u01dc\7\6\2\2\u01dc")
        buf.write("\u01dd\5\66\34\2\u01dd\u01de\b\37\1\2\u01de=\3\2\2\2\u01df")
        buf.write("\u01e0\7D\2\2\u01e0\u01e1\5\66\34\2\u01e1\u01e2\7C\2\2")
        buf.write("\u01e2\u01e3\7\5\2\2\u01e3\u01e4\5V,\2\u01e4\u01e5\7\6")
        buf.write("\2\2\u01e5\u01e6\7\4\2\2\u01e6\u01e7\b \1\2\u01e7?\3\2")
        buf.write("\2\2\u01e8\u01e9\7E\2\2\u01e9\u01eb\7\5\2\2\u01ea\u01ec")
        buf.write("\5V,\2\u01eb\u01ea\3\2\2\2\u01eb\u01ec\3\2\2\2\u01ec\u01ed")
        buf.write("\3\2\2\2\u01ed\u01ef\7\4\2\2\u01ee\u01f0\5V,\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2\u01f1")
        buf.write("\u01f3\7\4\2\2\u01f2\u01f4\5V,\2\u01f3\u01f2\3\2\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5\u01f6\7\6\2\2")
        buf.write("\u01f6\u01f7\5\66\34\2\u01f7\u01f8\b!\1\2\u01f8A\3\2\2")
        buf.write("\2\u01f9\u01fa\7@\2\2\u01fa\u01fb\7\5\2\2\u01fb\u01fc")
        buf.write("\5V,\2\u01fc\u01fd\7\6\2\2\u01fd\u01fe\7\n\2\2\u01fe\u01ff")
        buf.write("\5D#\2\u01ff\u0200\7\13\2\2\u0200\u0201\b\"\1\2\u0201")
        buf.write("C\3\2\2\2\u0202\u0203\5F$\2\u0203\u0204\b#\1\2\u0204\u0206")
        buf.write("\3\2\2\2\u0205\u0202\3\2\2\2\u0206\u0209\3\2\2\2\u0207")
        buf.write("\u0205\3\2\2\2\u0207\u0208\3\2\2\2\u0208\u020d\3\2\2\2")
        buf.write("\u0209\u0207\3\2\2\2\u020a\u020b\5J&\2\u020b\u020c\b#")
        buf.write("\1\2\u020c\u020e\3\2\2\2\u020d\u020a\3\2\2\2\u020d\u020e")
        buf.write("\3\2\2\2\u020e\u020f\3\2\2\2\u020f\u0210\b#\1\2\u0210")
        buf.write("E\3\2\2\2\u0211\u0212\5H%\2\u0212\u0213\5L\'\2\u0213\u0214")
        buf.write("\b$\1\2\u0214G\3\2\2\2\u0215\u0216\7A\2\2\u0216\u0217")
        buf.write("\5v<\2\u0217\u0218\7\17\2\2\u0218\u0219\b%\1\2\u0219\u021b")
        buf.write("\3\2\2\2\u021a\u0215\3\2\2\2\u021b\u021c\3\2\2\2\u021c")
        buf.write("\u021a\3\2\2\2\u021c\u021d\3\2\2\2\u021d\u021e\3\2\2\2")
        buf.write("\u021e\u021f\b%\1\2\u021fI\3\2\2\2\u0220\u0221\7B\2\2")
        buf.write("\u0221\u0222\7\17\2\2\u0222\u0223\5L\'\2\u0223\u0224\b")
        buf.write("&\1\2\u0224K\3\2\2\2\u0225\u0226\5\66\34\2\u0226\u0227")
        buf.write("\b\'\1\2\u0227\u0229\3\2\2\2\u0228\u0225\3\2\2\2\u0229")
        buf.write("\u022a\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2")
        buf.write("\u022b\u022c\3\2\2\2\u022c\u022d\b\'\1\2\u022dM\3\2\2")
        buf.write("\2\u022e\u022f\7G\2\2\u022f\u0230\7\4\2\2\u0230\u0231")
        buf.write("\b(\1\2\u0231O\3\2\2\2\u0232\u0233\7H\2\2\u0233\u0234")
        buf.write("\7\4\2\2\u0234\u0235\b)\1\2\u0235Q\3\2\2\2\u0236\u0237")
        buf.write("\7I\2\2\u0237\u0238\7M\2\2\u0238\u0239\7\4\2\2\u0239\u023a")
        buf.write("\b*\1\2\u023aS\3\2\2\2\u023b\u023c\7F\2\2\u023c\u023d")
        buf.write("\7\4\2\2\u023d\u0244\b+\1\2\u023e\u023f\7F\2\2\u023f\u0240")
        buf.write("\5V,\2\u0240\u0241\7\4\2\2\u0241\u0242\b+\1\2\u0242\u0244")
        buf.write("\3\2\2\2\u0243\u023b\3\2\2\2\u0243\u023e\3\2\2\2\u0244")
        buf.write("U\3\2\2\2\u0245\u0246\5n8\2\u0246\u0247\7\7\2\2\u0247")
        buf.write("\u0248\5V,\2\u0248\u0249\b,\1\2\u0249\u0253\3\2\2\2\u024a")
        buf.write("\u024b\5n8\2\u024b\u024c\5X-\2\u024c\u024d\5V,\2\u024d")
        buf.write("\u024e\b,\1\2\u024e\u0253\3\2\2\2\u024f\u0250\5Z.\2\u0250")
        buf.write("\u0251\b,\1\2\u0251\u0253\3\2\2\2\u0252\u0245\3\2\2\2")
        buf.write("\u0252\u024a\3\2\2\2\u0252\u024f\3\2\2\2\u0253W\3\2\2")
        buf.write("\2\u0254\u0255\7\20\2\2\u0255\u0269\b-\1\2\u0256\u0257")
        buf.write("\7\21\2\2\u0257\u0269\b-\1\2\u0258\u0259\7\22\2\2\u0259")
        buf.write("\u0269\b-\1\2\u025a\u025b\7\23\2\2\u025b\u0269\b-\1\2")
        buf.write("\u025c\u025d\7\24\2\2\u025d\u0269\b-\1\2\u025e\u025f\7")
        buf.write("\25\2\2\u025f\u0269\b-\1\2\u0260\u0261\7\26\2\2\u0261")
        buf.write("\u0269\b-\1\2\u0262\u0263\7\27\2\2\u0263\u0269\b-\1\2")
        buf.write("\u0264\u0265\7\30\2\2\u0265\u0269\b-\1\2\u0266\u0267\7")
        buf.write("\31\2\2\u0267\u0269\b-\1\2\u0268\u0254\3\2\2\2\u0268\u0256")
        buf.write("\3\2\2\2\u0268\u0258\3\2\2\2\u0268\u025a\3\2\2\2\u0268")
        buf.write("\u025c\3\2\2\2\u0268\u025e\3\2\2\2\u0268\u0260\3\2\2\2")
        buf.write("\u0268\u0262\3\2\2\2\u0268\u0264\3\2\2\2\u0268\u0266\3")
        buf.write("\2\2\2\u0269Y\3\2\2\2\u026a\u026b\5\\/\2\u026b\u0272\b")
        buf.write(".\1\2\u026c\u026d\7\32\2\2\u026d\u026e\5V,\2\u026e\u026f")
        buf.write("\7\17\2\2\u026f\u0270\5Z.\2\u0270\u0271\b.\1\2\u0271\u0273")
        buf.write("\3\2\2\2\u0272\u026c\3\2\2\2\u0272\u0273\3\2\2\2\u0273")
        buf.write("[\3\2\2\2\u0274\u027b\5^\60\2\u0275\u0276\7\33\2\2\u0276")
        buf.write("\u0277\5^\60\2\u0277\u0278\b/\1\2\u0278\u027a\3\2\2\2")
        buf.write("\u0279\u0275\3\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279\3")
        buf.write("\2\2\2\u027b\u027c\3\2\2\2\u027c\u027e\3\2\2\2\u027d\u027b")
        buf.write("\3\2\2\2\u027e\u027f\b/\1\2\u027f]\3\2\2\2\u0280\u0287")
        buf.write("\5`\61\2\u0281\u0282\7\34\2\2\u0282\u0283\5`\61\2\u0283")
        buf.write("\u0284\b\60\1\2\u0284\u0286\3\2\2\2\u0285\u0281\3\2\2")
        buf.write("\2\u0286\u0289\3\2\2\2\u0287\u0285\3\2\2\2\u0287\u0288")
        buf.write("\3\2\2\2\u0288\u028a\3\2\2\2\u0289\u0287\3\2\2\2\u028a")
        buf.write("\u028b\b\60\1\2\u028b_\3\2\2\2\u028c\u02a7\5b\62\2\u028d")
        buf.write("\u028e\7\35\2\2\u028e\u028f\5b\62\2\u028f\u0290\b\61\1")
        buf.write("\2\u0290\u02a6\3\2\2\2\u0291\u0292\7\36\2\2\u0292\u0293")
        buf.write("\5b\62\2\u0293\u0294\b\61\1\2\u0294\u02a6\3\2\2\2\u0295")
        buf.write("\u0296\7\37\2\2\u0296\u0297\5b\62\2\u0297\u0298\b\61\1")
        buf.write("\2\u0298\u02a6\3\2\2\2\u0299\u029a\7 \2\2\u029a\u029b")
        buf.write("\5b\62\2\u029b\u029c\b\61\1\2\u029c\u02a6\3\2\2\2\u029d")
        buf.write("\u029e\7!\2\2\u029e\u029f\5b\62\2\u029f\u02a0\b\61\1\2")
        buf.write("\u02a0\u02a6\3\2\2\2\u02a1\u02a2\7\"\2\2\u02a2\u02a3\5")
        buf.write("b\62\2\u02a3\u02a4\b\61\1\2\u02a4\u02a6\3\2\2\2\u02a5")
        buf.write("\u028d\3\2\2\2\u02a5\u0291\3\2\2\2\u02a5\u0295\3\2\2\2")
        buf.write("\u02a5\u0299\3\2\2\2\u02a5\u029d\3\2\2\2\u02a5\u02a1\3")
        buf.write("\2\2\2\u02a6\u02a9\3\2\2\2\u02a7\u02a5\3\2\2\2\u02a7\u02a8")
        buf.write("\3\2\2\2\u02a8\u02aa\3\2\2\2\u02a9\u02a7\3\2\2\2\u02aa")
        buf.write("\u02ab\b\61\1\2\u02aba\3\2\2\2\u02ac\u02b3\5d\63\2\u02ad")
        buf.write("\u02ae\7#\2\2\u02ae\u02af\5d\63\2\u02af\u02b0\b\62\1\2")
        buf.write("\u02b0\u02b2\3\2\2\2\u02b1\u02ad\3\2\2\2\u02b2\u02b5\3")
        buf.write("\2\2\2\u02b3\u02b1\3\2\2\2\u02b3\u02b4\3\2\2\2\u02b4\u02b6")
        buf.write("\3\2\2\2\u02b5\u02b3\3\2\2\2\u02b6\u02b7\b\62\1\2\u02b7")
        buf.write("c\3\2\2\2\u02b8\u02bf\5f\64\2\u02b9\u02ba\7$\2\2\u02ba")
        buf.write("\u02bb\5f\64\2\u02bb\u02bc\b\63\1\2\u02bc\u02be\3\2\2")
        buf.write("\2\u02bd\u02b9\3\2\2\2\u02be\u02c1\3\2\2\2\u02bf\u02bd")
        buf.write("\3\2\2\2\u02bf\u02c0\3\2\2\2\u02c0\u02c2\3\2\2\2\u02c1")
        buf.write("\u02bf\3\2\2\2\u02c2\u02c3\b\63\1\2\u02c3e\3\2\2\2\u02c4")
        buf.write("\u02cb\5h\65\2\u02c5\u02c6\7%\2\2\u02c6\u02c7\5h\65\2")
        buf.write("\u02c7\u02c8\b\64\1\2\u02c8\u02ca\3\2\2\2\u02c9\u02c5")
        buf.write("\3\2\2\2\u02ca\u02cd\3\2\2\2\u02cb\u02c9\3\2\2\2\u02cb")
        buf.write("\u02cc\3\2\2\2\u02cc\u02ce\3\2\2\2\u02cd\u02cb\3\2\2\2")
        buf.write("\u02ce\u02cf\b\64\1\2\u02cfg\3\2\2\2\u02d0\u02db\5j\66")
        buf.write("\2\u02d1\u02d2\7&\2\2\u02d2\u02d3\5j\66\2\u02d3\u02d4")
        buf.write("\b\65\1\2\u02d4\u02da\3\2\2\2\u02d5\u02d6\7\'\2\2\u02d6")
        buf.write("\u02d7\5j\66\2\u02d7\u02d8\b\65\1\2\u02d8\u02da\3\2\2")
        buf.write("\2\u02d9\u02d1\3\2\2\2\u02d9\u02d5\3\2\2\2\u02da\u02dd")
        buf.write("\3\2\2\2\u02db\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc")
        buf.write("\u02de\3\2\2\2\u02dd\u02db\3\2\2\2\u02de\u02df\b\65\1")
        buf.write("\2\u02dfi\3\2\2\2\u02e0\u02eb\5l\67\2\u02e1\u02e2\7(\2")
        buf.write("\2\u02e2\u02e3\5l\67\2\u02e3\u02e4\b\66\1\2\u02e4\u02ea")
        buf.write("\3\2\2\2\u02e5\u02e6\7)\2\2\u02e6\u02e7\5l\67\2\u02e7")
        buf.write("\u02e8\b\66\1\2\u02e8\u02ea\3\2\2\2\u02e9\u02e1\3\2\2")
        buf.write("\2\u02e9\u02e5\3\2\2\2\u02ea\u02ed\3\2\2\2\u02eb\u02e9")
        buf.write("\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec\u02ee\3\2\2\2\u02ed")
        buf.write("\u02eb\3\2\2\2\u02ee\u02ef\b\66\1\2\u02efk\3\2\2\2\u02f0")
        buf.write("\u02ff\5n8\2\u02f1\u02f2\7\16\2\2\u02f2\u02f3\5n8\2\u02f3")
        buf.write("\u02f4\b\67\1\2\u02f4\u02fe\3\2\2\2\u02f5\u02f6\7*\2\2")
        buf.write("\u02f6\u02f7\5n8\2\u02f7\u02f8\b\67\1\2\u02f8\u02fe\3")
        buf.write("\2\2\2\u02f9\u02fa\7+\2\2\u02fa\u02fb\5n8\2\u02fb\u02fc")
        buf.write("\b\67\1\2\u02fc\u02fe\3\2\2\2\u02fd\u02f1\3\2\2\2\u02fd")
        buf.write("\u02f5\3\2\2\2\u02fd\u02f9\3\2\2\2\u02fe\u0301\3\2\2\2")
        buf.write("\u02ff\u02fd\3\2\2\2\u02ff\u0300\3\2\2\2\u0300\u0302\3")
        buf.write("\2\2\2\u0301\u02ff\3\2\2\2\u0302\u0303\b\67\1\2\u0303")
        buf.write("m\3\2\2\2\u0304\u0305\7\5\2\2\u0305\u0306\5*\26\2\u0306")
        buf.write("\u0307\7\6\2\2\u0307\u0308\5n8\2\u0308\u0309\b8\1\2\u0309")
        buf.write("\u030e\3\2\2\2\u030a\u030b\5p9\2\u030b\u030c\b8\1\2\u030c")
        buf.write("\u030e\3\2\2\2\u030d\u0304\3\2\2\2\u030d\u030a\3\2\2\2")
        buf.write("\u030eo\3\2\2\2\u030f\u0310\7,\2\2\u0310\u0311\5p9\2\u0311")
        buf.write("\u0312\b9\1\2\u0312\u033d\3\2\2\2\u0313\u0314\7-\2\2\u0314")
        buf.write("\u0315\5p9\2\u0315\u0316\b9\1\2\u0316\u033d\3\2\2\2\u0317")
        buf.write("\u0318\7(\2\2\u0318\u0319\5n8\2\u0319\u031a\b9\1\2\u031a")
        buf.write("\u033d\3\2\2\2\u031b\u031c\7)\2\2\u031c\u031d\5n8\2\u031d")
        buf.write("\u031e\b9\1\2\u031e\u033d\3\2\2\2\u031f\u0320\7.\2\2\u0320")
        buf.write("\u0321\5n8\2\u0321\u0322\b9\1\2\u0322\u033d\3\2\2\2\u0323")
        buf.write("\u0324\7/\2\2\u0324\u0325\5n8\2\u0325\u0326\b9\1\2\u0326")
        buf.write("\u033d\3\2\2\2\u0327\u0328\7\16\2\2\u0328\u0329\5n8\2")
        buf.write("\u0329\u032a\b9\1\2\u032a\u033d\3\2\2\2\u032b\u032c\7")
        buf.write("%\2\2\u032c\u032d\5n8\2\u032d\u032e\b9\1\2\u032e\u033d")
        buf.write("\3\2\2\2\u032f\u0330\7L\2\2\u0330\u0331\7\5\2\2\u0331")
        buf.write("\u0332\5*\26\2\u0332\u0333\7\6\2\2\u0333\u0334\b9\1\2")
        buf.write("\u0334\u033d\3\2\2\2\u0335\u0336\7L\2\2\u0336\u0337\5")
        buf.write("p9\2\u0337\u0338\b9\1\2\u0338\u033d\3\2\2\2\u0339\u033a")
        buf.write("\5r:\2\u033a\u033b\b9\1\2\u033b\u033d\3\2\2\2\u033c\u030f")
        buf.write("\3\2\2\2\u033c\u0313\3\2\2\2\u033c\u0317\3\2\2\2\u033c")
        buf.write("\u031b\3\2\2\2\u033c\u031f\3\2\2\2\u033c\u0323\3\2\2\2")
        buf.write("\u033c\u0327\3\2\2\2\u033c\u032b\3\2\2\2\u033c\u032f\3")
        buf.write("\2\2\2\u033c\u0335\3\2\2\2\u033c\u0339\3\2\2\2\u033dq")
        buf.write("\3\2\2\2\u033e\u033f\5v<\2\u033f\u0358\b:\1\2\u0340\u0341")
        buf.write("\7,\2\2\u0341\u0357\b:\1\2\u0342\u0343\7-\2\2\u0343\u0357")
        buf.write("\b:\1\2\u0344\u0345\7\f\2\2\u0345\u0346\5V,\2\u0346\u0347")
        buf.write("\7\r\2\2\u0347\u0348\b:\1\2\u0348\u0357\3\2\2\2\u0349")
        buf.write("\u034a\7\3\2\2\u034a\u034b\5\n\6\2\u034b\u034c\b:\1\2")
        buf.write("\u034c\u0357\3\2\2\2\u034d\u034e\7\60\2\2\u034e\u034f")
        buf.write("\5\n\6\2\u034f\u0350\b:\1\2\u0350\u0357\3\2\2\2\u0351")
        buf.write("\u0352\7\5\2\2\u0352\u0353\5t;\2\u0353\u0354\7\6\2\2\u0354")
        buf.write("\u0355\b:\1\2\u0355\u0357\3\2\2\2\u0356\u0340\3\2\2\2")
        buf.write("\u0356\u0342\3\2\2\2\u0356\u0344\3\2\2\2\u0356\u0349\3")
        buf.write("\2\2\2\u0356\u034d\3\2\2\2\u0356\u0351\3\2\2\2\u0357\u035a")
        buf.write("\3\2\2\2\u0358\u0356\3\2\2\2\u0358\u0359\3\2\2\2\u0359")
        buf.write("\u035b\3\2\2\2\u035a\u0358\3\2\2\2\u035b\u035c\b:\1\2")
        buf.write("\u035cs\3\2\2\2\u035d\u035e\5V,\2\u035e\u0365\b;\1\2\u035f")
        buf.write("\u0360\7\b\2\2\u0360\u0361\5V,\2\u0361\u0362\b;\1\2\u0362")
        buf.write("\u0364\3\2\2\2\u0363\u035f\3\2\2\2\u0364\u0367\3\2\2\2")
        buf.write("\u0365\u0363\3\2\2\2\u0365\u0366\3\2\2\2\u0366\u0369\3")
        buf.write("\2\2\2\u0367\u0365\3\2\2\2\u0368\u035d\3\2\2\2\u0368\u0369")
        buf.write("\3\2\2\2\u0369\u036a\3\2\2\2\u036a\u036b\b;\1\2\u036b")
        buf.write("u\3\2\2\2\u036c\u036d\7N\2\2\u036d\u037a\b<\1\2\u036e")
        buf.write("\u036f\7S\2\2\u036f\u037a\b<\1\2\u0370\u0371\7R\2\2\u0371")
        buf.write("\u037a\b<\1\2\u0372\u0373\7M\2\2\u0373\u037a\b<\1\2\u0374")
        buf.write("\u0375\7\5\2\2\u0375\u0376\5V,\2\u0376\u0377\7\6\2\2\u0377")
        buf.write("\u0378\b<\1\2\u0378\u037a\3\2\2\2\u0379\u036c\3\2\2\2")
        buf.write("\u0379\u036e\3\2\2\2\u0379\u0370\3\2\2\2\u0379\u0372\3")
        buf.write("\2\2\2\u0379\u0374\3\2\2\2\u037aw\3\2\2\2\u037b\u037c")
        buf.write("\b=\1\2\u037c\u037d\5\2\2\2\u037d\u037e\5\f\7\2\u037e")
        buf.write("\u037f\b=\1\2\u037fy\3\2\2\2\u0380\u0381\5\2\2\2\u0381")
        buf.write("\u0396\b>\1\2\u0382\u0383\5\6\4\2\u0383\u0384\b>\1\2\u0384")
        buf.write("\u0395\3\2\2\2\u0385\u0386\5\b\5\2\u0386\u0387\b>\1\2")
        buf.write("\u0387\u0395\3\2\2\2\u0388\u0389\5\36\20\2\u0389\u038a")
        buf.write("\b>\1\2\u038a\u0395\3\2\2\2\u038b\u038c\5 \21\2\u038c")
        buf.write("\u038d\b>\1\2\u038d\u0395\3\2\2\2\u038e\u038f\5\"\22\2")
        buf.write("\u038f\u0390\b>\1\2\u0390\u0395\3\2\2\2\u0391\u0392\5")
        buf.write("(\25\2\u0392\u0393\b>\1\2\u0393\u0395\3\2\2\2\u0394\u0382")
        buf.write("\3\2\2\2\u0394\u0385\3\2\2\2\u0394\u0388\3\2\2\2\u0394")
        buf.write("\u038b\3\2\2\2\u0394\u038e\3\2\2\2\u0394\u0391\3\2\2\2")
        buf.write("\u0395\u0398\3\2\2\2\u0396\u0394\3\2\2\2\u0396\u0397\3")
        buf.write("\2\2\2\u0397\u0399\3\2\2\2\u0398\u0396\3\2\2\2\u0399\u039a")
        buf.write("\b>\1\2\u039a{\3\2\2\29\u0081\u008f\u00b9\u00bb\u00c7")
        buf.write("\u00d0\u00d6\u00dd\u00f0\u00f4\u00fe\u0112\u0132\u0154")
        buf.write("\u0156\u0161\u0165\u016f\u0193\u019a\u01c6\u01d4\u01eb")
        buf.write("\u01ef\u01f3\u0207\u020d\u021c\u022a\u0243\u0252\u0268")
        buf.write("\u0272\u027b\u0287\u02a5\u02a7\u02b3\u02bf\u02cb\u02d9")
        buf.write("\u02db\u02e9\u02eb\u02fd\u02ff\u030d\u033c\u0356\u0358")
        buf.write("\u0365\u0368\u0379\u0394\u0396")
        return buf.getvalue()


class CprestoParser ( Parser ):

    grammarFileName = "Cpresto.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "';'", "'('", "')'", "'='", "','", 
                     "'...'", "'{'", "'}'", "'['", "']'", "'*'", "':'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'&='", "'|='", 
                     "'^='", "'<<='", "'>>='", "'?'", "'||'", "'&&'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'|'", "'^'", 
                     "'&'", "'>>'", "'<<'", "'+'", "'-'", "'/'", "'%'", 
                     "'++'", "'--'", "'!'", "'~'", "'->'", "'void'", "'char'", 
                     "'short'", "'int'", "'long'", "'struct'", "'union'", 
                     "'enum'", "'static'", "'extern'", "'const'", "'signed'", 
                     "'unsigned'", "'if'", "'else'", "'switch'", "'case'", 
                     "'default'", "'while'", "'do'", "'for'", "'return'", 
                     "'break'", "'continue'", "'goto'", "'typedef'", "'import'", 
                     "'sizeof'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "VOID", "CHAR", 
                      "SHORT", "INT", "LONG", "STRUCT", "UNION", "ENUM", 
                      "STATIC", "EXTERN", "CONST", "SIGNED", "UNSIGNED", 
                      "IF", "ELSE", "SWITCH", "CASE", "DEFAULT", "WHILE", 
                      "DO", "FOR", "RETURN", "BREAK", "CONTINUE", "GOTO", 
                      "TYPEDEF", "IMPORT", "SIZEOF", "IDENTIFIER", "INTEGER", 
                      "SPACES", "LINE_COMMENT", "BLOCK_COMMENT", "STRING", 
                      "CHARACTER" ]

    RULE_import_stmts = 0
    RULE_import_stmt = 1
    RULE_funcdecl = 2
    RULE_vardecl = 3
    RULE_name = 4
    RULE_top_defs = 5
    RULE_defvars = 6
    RULE_storage = 7
    RULE_defun = 8
    RULE_params = 9
    RULE_fixedparams = 10
    RULE_param = 11
    RULE_block = 12
    RULE_defvar_list = 13
    RULE_defconst = 14
    RULE_defstruct = 15
    RULE_defunion = 16
    RULE_member_list = 17
    RULE_slot = 18
    RULE_typedef = 19
    RULE_typename = 20
    RULE_typeref = 21
    RULE_param_typerefs = 22
    RULE_fixedparam_typerefs = 23
    RULE_typeref_base = 24
    RULE_stmts = 25
    RULE_stmt = 26
    RULE_labeled_stmt = 27
    RULE_if_stmt = 28
    RULE_while_stmt = 29
    RULE_dowhile_stmt = 30
    RULE_for_stmt = 31
    RULE_switch_stmt = 32
    RULE_case_clauses = 33
    RULE_case_clause = 34
    RULE_cases = 35
    RULE_default_clause = 36
    RULE_case_body = 37
    RULE_break_stmt = 38
    RULE_continue_stmt = 39
    RULE_goto_stmt = 40
    RULE_return_stmt = 41
    RULE_expr = 42
    RULE_opassign_op = 43
    RULE_expr10 = 44
    RULE_expr9 = 45
    RULE_expr8 = 46
    RULE_expr7 = 47
    RULE_expr6 = 48
    RULE_expr5 = 49
    RULE_expr4 = 50
    RULE_expr3 = 51
    RULE_expr2 = 52
    RULE_expr1 = 53
    RULE_term = 54
    RULE_unary = 55
    RULE_postfix = 56
    RULE_args = 57
    RULE_primary = 58
    RULE_compilation_unit = 59
    RULE_declaration_file = 60

    ruleNames =  [ "import_stmts", "import_stmt", "funcdecl", "vardecl", 
                   "name", "top_defs", "defvars", "storage", "defun", "params", 
                   "fixedparams", "param", "block", "defvar_list", "defconst", 
                   "defstruct", "defunion", "member_list", "slot", "typedef", 
                   "typename", "typeref", "param_typerefs", "fixedparam_typerefs", 
                   "typeref_base", "stmts", "stmt", "labeled_stmt", "if_stmt", 
                   "while_stmt", "dowhile_stmt", "for_stmt", "switch_stmt", 
                   "case_clauses", "case_clause", "cases", "default_clause", 
                   "case_body", "break_stmt", "continue_stmt", "goto_stmt", 
                   "return_stmt", "expr", "opassign_op", "expr10", "expr9", 
                   "expr8", "expr7", "expr6", "expr5", "expr4", "expr3", 
                   "expr2", "expr1", "term", "unary", "postfix", "args", 
                   "primary", "compilation_unit", "declaration_file" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    T__41=42
    T__42=43
    T__43=44
    T__44=45
    T__45=46
    VOID=47
    CHAR=48
    SHORT=49
    INT=50
    LONG=51
    STRUCT=52
    UNION=53
    ENUM=54
    STATIC=55
    EXTERN=56
    CONST=57
    SIGNED=58
    UNSIGNED=59
    IF=60
    ELSE=61
    SWITCH=62
    CASE=63
    DEFAULT=64
    WHILE=65
    DO=66
    FOR=67
    RETURN=68
    BREAK=69
    CONTINUE=70
    GOTO=71
    TYPEDEF=72
    IMPORT=73
    SIZEOF=74
    IDENTIFIER=75
    INTEGER=76
    SPACES=77
    LINE_COMMENT=78
    BLOCK_COMMENT=79
    STRING=80
    CHARACTER=81

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    def parse(self):
            try:
                    return self.compilation_unit()
            except Exception as ex:
                    raise SyntaxException(ex.message)

    def parse_decls(self):
            try:
                    return self.declaration_file()
            except Exception as ex:
                    raise SyntaxException(ex.message)

    def add_known_typedefs(self,typedefs):
            for n in typedefs:
                    self.add_type(n.name())

    def add_type(self,name):
            self.known_typedefs.add(name)

    def is_type(self,name): 
            return name in self.known_typedefs

    def integer_node(self,loc,image):
            i = self.integer_value(image)
            if image.endswith("UL"):
                    return IntegerLiteralNode(loc,IntegerTypeRef.ulong_ref(),i)
            elif image.endswith("L"):
                    return IntegerLiteralNode(loc,IntegerTypeRef.long_ref(),i)
            elif image.endswith("U"):
                    return IntegerLiteralNode(loc,IntegerTypeRef.uint_ref(),i)
            else:
                    return IntegerLiteralNode(loc,IntegerTypeRef.int_ref(),i)

    def integer_value(self,image):
            s = image.replace("U","").replace("L","")
            if s.startswith("0x") or s.startswith("0X"):
                    return int(s, 16)
            elif s.startswith("0") and (s != "0"):
                    return int(s,8)
            else :
                    return int(s)

    def character_code(self,image):
            s = self.string_value(image)
            if len(s) != 1:
                    raise Exception("must not happen: character length > 1")
            return ord(s)

    def string_value(self,_image):
            pos = 0
            buf = ""
            image = _image[1:-1]
            idx = image.index("\\",pos)
            while idx >= 0:
                    buf += image[pos:idx]
                    if len(image) >= idx + 4 and image[idx+1].isdigit() and \
                       image[idx+2].isdigit() and image[idx+3].isdigit():
                            buf += self.unescape_octal(image[idx+1:idx+4])
                            pos = idx + 4
                    else :
                            buf += self.unescape_seq(image[idx+1])
                            pos = idx + 2
                    idx = image.index("\\",pos)
            if pos < len(image):
                    buf += image[pos:len(image)]
            return buf

    def size_t(self):
            return IntegerTypeRef.ulong_ref()

    char_max = 255

    def unescape_octal(self,digits):
            i = int(digits,8)
            if i > CprestoParser.char_max:
                    raise ParseException("octal character sequence too big: \\" + digits)
            return chr(i)

    bell = 7
    backspace = 8
    escape = 27
    vt = 11

    def unescape_seq(self,c):
            if c == '0':
                    return '\0'
            elif c == '"':
                    return '"'
            elif c == '\'':
                    return '\''
            elif c == 'a':
                    return chr(CprestoParser.bell)
            elif c == 'b':
                    return chr(CprestoParser.backspace)
            elif c == 'e':
                    return chr(CprestoParser.escape)
            elif c == 'f':
                    return '\f'
            elif c == 'n':
                    return '\n'
            elif c == 'r':
                    return '\r'
            elif c == 't':
                    return '\t'
            elif c == 'v':
                    return chr(CprestoParser.vt)
            else :
                    raise ParseException("unknown escape sequence: \"\\" + c)

    def location(self,t):
            kindname = CprestoParser.symbolicNames[t.type]
            return Location(self.source_name,t,kindname)




    class Import_stmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.decls = None
            self.impdecls = Declarations()
            self.libid = None # Import_stmtContext

        def import_stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Import_stmtContext)
            else:
                return self.getTypedRuleContext(CprestoParser.Import_stmtContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_import_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_stmts" ):
                listener.enterImport_stmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_stmts" ):
                listener.exitImport_stmts(self)




    def import_stmts(self):

        localctx = CprestoParser.Import_stmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_import_stmts)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 122
                    localctx.libid = self.import_stmt()

                    try:
                            localctx.decls = self.loader.load_library(localctx.libid.res,self.error_handler)
                            if localctx.decls != None:
                                    localctx.impdecls.add(localctx.decls)
                                    self.add_known_typedefs(localctx.decls.typedefs())
                    except CompileException as ex:
                            raise RecognitionException(message=ex.message)
             
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)


            localctx.res = localctx.impdecls

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.buf = ""
            self.n = None # NameContext

        def IMPORT(self):
            return self.getToken(CprestoParser.IMPORT, 0)

        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.NameContext)
            else:
                return self.getTypedRuleContext(CprestoParser.NameContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_import_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImport_stmt" ):
                listener.enterImport_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImport_stmt" ):
                listener.exitImport_stmt(self)




    def import_stmt(self):

        localctx = CprestoParser.Import_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_import_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(CprestoParser.IMPORT)
            self.state = 133
            localctx.n = self.name()

            localctx.buf += (None if localctx.n is None else self._input.getText(localctx.n.start,localctx.n.stop))

            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__0:
                self.state = 135
                self.match(CprestoParser.T__0)
                self.state = 136
                localctx.n = self.name()

                localctx.buf += '.' + (None if localctx.n is None else self._input.getText(localctx.n.start,localctx.n.stop))

                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 144
            self.match(CprestoParser.T__1)

            localctx.res = localctx.buf

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None
            self.ret = None # TyperefContext
            self.n = None # NameContext
            self.ps = None # ParamsContext

        def EXTERN(self):
            return self.getToken(CprestoParser.EXTERN, 0)

        def typeref(self):
            return self.getTypedRuleContext(CprestoParser.TyperefContext,0)


        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def params(self):
            return self.getTypedRuleContext(CprestoParser.ParamsContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_funcdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncdecl" ):
                listener.enterFuncdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncdecl" ):
                listener.exitFuncdecl(self)




    def funcdecl(self):

        localctx = CprestoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(CprestoParser.EXTERN)
            self.state = 148
            localctx.ret = self.typeref()
            self.state = 149
            localctx.n = self.name()
            self.state = 150
            self.match(CprestoParser.T__2)
            self.state = 151
            localctx.ps = self.params()
            self.state = 152
            self.match(CprestoParser.T__3)
            self.state = 153
            self.match(CprestoParser.T__1)

            localctx.t = FunctionTypeRef(ret,ps.parameters_type_ref())
            localctx.res = UndefinedFunction(TypeNode(localctx.t),n,ps)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # TypenameContext
            self.n = None # NameContext

        def EXTERN(self):
            return self.getToken(CprestoParser.EXTERN, 0)

        def typename(self):
            return self.getTypedRuleContext(CprestoParser.TypenameContext,0)


        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_vardecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVardecl" ):
                listener.enterVardecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVardecl" ):
                listener.exitVardecl(self)




    def vardecl(self):

        localctx = CprestoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(CprestoParser.EXTERN)
            self.state = 157
            localctx.t = self.typename()
            self.state = 158
            localctx.n = self.name()
            self.state = 159
            self.match(CprestoParser.T__1)

            localctx.res = UndefinedVariable(localctx.t.res,localctx.n.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token

        def IDENTIFIER(self):
            return self.getToken(CprestoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = CprestoParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            localctx.t = self.match(CprestoParser.IDENTIFIER)

            localctx.res = (None if localctx.t is None else localctx.t.text)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Top_defsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.decls = Declarations()
            self.df = None # DefunContext
            self.dv = None # DefvarsContext
            self.dc = None # DefconstContext
            self.ds = None # DefstructContext
            self.du = None # DefunionContext
            self.td = None # TypedefContext

        def defun(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefunContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefunContext,i)


        def defvars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefvarsContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefvarsContext,i)


        def defconst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefconstContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefconstContext,i)


        def defstruct(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefstructContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefstructContext,i)


        def defunion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefunionContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefunionContext,i)


        def typedef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.TypedefContext)
            else:
                return self.getTypedRuleContext(CprestoParser.TypedefContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_top_defs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop_defs" ):
                listener.enterTop_defs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop_defs" ):
                listener.exitTop_defs(self)




    def top_defs(self):

        localctx = CprestoParser.Top_defsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_top_defs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 183
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        self.state = 165
                        localctx.df = self.defun()
                         
                        localctx.decls.add_defun(localctx.df.res) 

                        pass

                    elif la_ == 2:
                        self.state = 168
                        localctx.dv = self.defvars()
                         
                        localctx.decls.add_defvars(localctx.dv.res) 

                        pass

                    elif la_ == 3:
                        self.state = 171
                        localctx.dc = self.defconst()
                         
                        localctx.decls.add_constant(localctx.dc.res) 

                        pass

                    elif la_ == 4:
                        self.state = 174
                        localctx.ds = self.defstruct()
                         
                        localctx.decls.add_defstruct(localctx.ds.res) 

                        pass

                    elif la_ == 5:
                        self.state = 177
                        localctx.du = self.defunion()
                         
                        localctx.decls.add_defunion(localctx.du.res) 

                        pass

                    elif la_ == 6:
                        self.state = 180
                        localctx.td = self.typedef()
                         
                        localctx.decls.add_typedef(localctx.td.res) 

                        pass

             
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

             
            localctx.res = localctx.decls 

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefvarsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.defs = list()
            self.initflag = False
            self.priv = None # StorageContext
            self.t = None # TypenameContext
            self.n = None # NameContext
            self.init = None # ExprContext

        def storage(self):
            return self.getTypedRuleContext(CprestoParser.StorageContext,0)


        def typename(self):
            return self.getTypedRuleContext(CprestoParser.TypenameContext,0)


        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.NameContext)
            else:
                return self.getTypedRuleContext(CprestoParser.NameContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.ExprContext)
            else:
                return self.getTypedRuleContext(CprestoParser.ExprContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_defvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefvars" ):
                listener.enterDefvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefvars" ):
                listener.exitDefvars(self)




    def defvars(self):

        localctx = CprestoParser.DefvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_defvars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            localctx.priv = self.storage()
            self.state = 191
            localctx.t = self.typename()
            self.state = 192
            localctx.n = self.name()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CprestoParser.T__4:
                self.state = 193
                self.match(CprestoParser.T__4)
                self.state = 194
                localctx.init = self.expr()

                if init != None:
                        localctx.initflag = True




            localctx.defs.append(DefinedVariable(priv,t,n,None) if not localctx.initflag else DefinedVariable(priv,t,n,init))
            localctx.initflag=False

            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__5:
                self.state = 200
                self.match(CprestoParser.T__5)
                self.state = 201
                localctx.n = self.name()
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CprestoParser.T__4:
                    self.state = 202
                    self.match(CprestoParser.T__4)
                    self.state = 203
                    localctx.init = self.expr()

                    if init != None:
                            localctx.initflag = True




                localctx.defs.append(DefinedVariable(priv,t,n,None) if not localctx.initflag else DefinedVariable(priv,t,n,init))
                localctx.initflag=False

                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 215
            self.match(CprestoParser.T__1)

            localctx.res = localctx.defs

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StorageContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token

        def STATIC(self):
            return self.getToken(CprestoParser.STATIC, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_storage

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStorage" ):
                listener.enterStorage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStorage" ):
                listener.exitStorage(self)




    def storage(self):

        localctx = CprestoParser.StorageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_storage)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 218
                localctx.t = self.match(CprestoParser.STATIC)



            localctx.res = False if localctx.t == None else True

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefunContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None
            self.priv = None # StorageContext
            self.ret = None # TyperefContext
            self.n = None # NameContext
            self.ps = None # ParamsContext
            self.body = None # BlockContext

        def storage(self):
            return self.getTypedRuleContext(CprestoParser.StorageContext,0)


        def typeref(self):
            return self.getTypedRuleContext(CprestoParser.TyperefContext,0)


        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def params(self):
            return self.getTypedRuleContext(CprestoParser.ParamsContext,0)


        def block(self):
            return self.getTypedRuleContext(CprestoParser.BlockContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_defun

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefun" ):
                listener.enterDefun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefun" ):
                listener.exitDefun(self)




    def defun(self):

        localctx = CprestoParser.DefunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_defun)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            localctx.priv = self.storage()
            self.state = 224
            localctx.ret = self.typeref()
            self.state = 225
            localctx.n = self.name()
            self.state = 226
            self.match(CprestoParser.T__2)
            self.state = 227
            localctx.ps = self.params()
            self.state = 228
            self.match(CprestoParser.T__3)
            self.state = 229
            localctx.body = self.block()

            localctx.t =  FunctionTypeRef(localctx.ret.res,localctx.ps.res.parameters_type_ref()) 
            localctx.res = DefinedFunction(localctx.priv.res,TypeNode(localctx.t),localctx.n.res,localctx.ps.res,localctx.body.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.pms = None # FixedparamsContext

        def VOID(self):
            return self.getToken(CprestoParser.VOID, 0)

        def fixedparams(self):
            return self.getTypedRuleContext(CprestoParser.FixedparamsContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_params

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParams" ):
                listener.enterParams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParams" ):
                listener.exitParams(self)




    def params(self):

        localctx = CprestoParser.ParamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_params)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 232
                localctx.t = self.match(CprestoParser.VOID)

                localctx.res = Params(self.location(localctx.t),[])

                pass

            elif la_ == 2:
                self.state = 234
                localctx.pms = self.fixedparams()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CprestoParser.T__5:
                    self.state = 235
                    self.match(CprestoParser.T__5)
                    self.state = 236
                    self.match(CprestoParser.T__6)

                    localctx.pms.res.accept_varargs()




                localctx.res = localctx.pms.res

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FixedparamsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.pms = list()
            self.pm1 = None # ParamContext
            self.pm = None # ParamContext

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.ParamContext)
            else:
                return self.getTypedRuleContext(CprestoParser.ParamContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_fixedparams

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedparams" ):
                listener.enterFixedparams(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedparams" ):
                listener.exitFixedparams(self)




    def fixedparams(self):

        localctx = CprestoParser.FixedparamsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_fixedparams)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            localctx.pm1 = self.param()

            localctx.pms.append(localctx.pm1.res)

            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 246
                    self.match(CprestoParser.T__5)
                    self.state = 247
                    localctx.pm = self.param()

                    if localctx.pm != None:
                            localctx.pms.append(localctx.pm.res)
             
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)


            localctx.res = Params(localctx.pm1.res.location(),localctx.pms)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # TypenameContext
            self.n = None # NameContext

        def typename(self):
            return self.getTypedRuleContext(CprestoParser.TypenameContext,0)


        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)




    def param(self):

        localctx = CprestoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            localctx.t = self.typename()
            self.state = 258
            localctx.n = self.name()

            localctx.res = Parameter(localctx.t.res,localctx.n.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.v = None # Defvar_listContext
            self.s = None # StmtsContext

        def defvar_list(self):
            return self.getTypedRuleContext(CprestoParser.Defvar_listContext,0)


        def stmts(self):
            return self.getTypedRuleContext(CprestoParser.StmtsContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = CprestoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            localctx.t = self.match(CprestoParser.T__7)
            self.state = 262
            localctx.v = self.defvar_list()
            self.state = 263
            localctx.s = self.stmts()
            self.state = 264
            self.match(CprestoParser.T__8)

            localctx.res = BlockNode(self.location(localctx.t),localctx.v.res,localctx.s.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Defvar_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = list()
            self.vs = None # DefvarsContext

        def defvars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefvarsContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefvarsContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_defvar_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefvar_list" ):
                listener.enterDefvar_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefvar_list" ):
                listener.exitDefvar_list(self)




    def defvar_list(self):

        localctx = CprestoParser.Defvar_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_defvar_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 267
                    localctx.vs = self.defvars()
                     
                    if vs != None:
                            localctx.l += vs
             
                self.state = 274
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)


            localctx.res = localctx.l

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefconstContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # TypenameContext
            self.n = None # NameContext
            self.v = None # ExprContext

        def CONST(self):
            return self.getToken(CprestoParser.CONST, 0)

        def typename(self):
            return self.getTypedRuleContext(CprestoParser.TypenameContext,0)


        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_defconst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefconst" ):
                listener.enterDefconst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefconst" ):
                listener.exitDefconst(self)




    def defconst(self):

        localctx = CprestoParser.DefconstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_defconst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(CprestoParser.CONST)
            self.state = 278
            localctx.t = self.typename()
            self.state = 279
            localctx.n = self.name()
            self.state = 280
            self.match(CprestoParser.T__4)
            self.state = 281
            localctx.v = self.expr()
            self.state = 282
            self.match(CprestoParser.T__1)

            localctx.res = Constant(t,n,v)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefstructContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.n = None # NameContext
            self.membs = None # Member_listContext

        def STRUCT(self):
            return self.getToken(CprestoParser.STRUCT, 0)

        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def member_list(self):
            return self.getTypedRuleContext(CprestoParser.Member_listContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_defstruct

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefstruct" ):
                listener.enterDefstruct(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefstruct" ):
                listener.exitDefstruct(self)




    def defstruct(self):

        localctx = CprestoParser.DefstructContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_defstruct)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            localctx.t = self.match(CprestoParser.STRUCT)
            self.state = 286
            localctx.n = self.name()
            self.state = 287
            localctx.membs = self.member_list()
            self.state = 288
            self.match(CprestoParser.T__1)

            localctx.res = StructNode(self.location(t),StructTypeRef(n),n,membs)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefunionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.n = None # NameContext
            self.membs = None # Member_listContext

        def UNION(self):
            return self.getToken(CprestoParser.UNION, 0)

        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def member_list(self):
            return self.getTypedRuleContext(CprestoParser.Member_listContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_defunion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefunion" ):
                listener.enterDefunion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefunion" ):
                listener.exitDefunion(self)




    def defunion(self):

        localctx = CprestoParser.DefunionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_defunion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 291
            localctx.t = self.match(CprestoParser.UNION)
            self.state = 292
            localctx.n = self.name()
            self.state = 293
            localctx.membs = self.member_list()
            self.state = 294
            self.match(CprestoParser.T__1)

            localctx.res = UnionNode(self.location(t),UnionTypeRef(n),n,membs)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.membs = list()
            self.s = None # SlotContext

        def slot(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.SlotContext)
            else:
                return self.getTypedRuleContext(CprestoParser.SlotContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_member_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_list" ):
                listener.enterMember_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_list" ):
                listener.exitMember_list(self)




    def member_list(self):

        localctx = CprestoParser.Member_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_member_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(CprestoParser.T__7)
            self.state = 304
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 298
                    localctx.s = self.slot()
                    self.state = 299
                    self.match(CprestoParser.T__1)

                    if s != None:
                            localctx.membs.append(s)
             
                self.state = 306
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 307
            self.match(CprestoParser.T__8)

            localctx.res = localctx.membs

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SlotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # TypenameContext
            self.n = None # NameContext

        def typename(self):
            return self.getTypedRuleContext(CprestoParser.TypenameContext,0)


        def name(self):
            return self.getTypedRuleContext(CprestoParser.NameContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_slot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlot" ):
                listener.enterSlot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlot" ):
                listener.exitSlot(self)




    def slot(self):

        localctx = CprestoParser.SlotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_slot)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            localctx.t = self.typename()
            self.state = 311
            localctx.n = self.name()

            localctx.res = Slot(t,n)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.ref = None # TyperefContext
            self.newname = None # Token

        def TYPEDEF(self):
            return self.getToken(CprestoParser.TYPEDEF, 0)

        def typeref(self):
            return self.getTypedRuleContext(CprestoParser.TyperefContext,0)


        def IDENTIFIER(self):
            return self.getToken(CprestoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_typedef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedef" ):
                listener.enterTypedef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedef" ):
                listener.exitTypedef(self)




    def typedef(self):

        localctx = CprestoParser.TypedefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typedef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            localctx.t = self.match(CprestoParser.TYPEDEF)
            self.state = 315
            localctx.ref = self.typeref()
            self.state = 316
            localctx.newname = self.match(CprestoParser.IDENTIFIER)
            self.state = 317
            self.match(CprestoParser.T__1)

            self.add_type((None if localctx.newname is None else localctx.newname.text))
            localctx.res = TypedefNode(self.location(t),ref,(None if localctx.newname is None else localctx.newname.text))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypenameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.ref = None # TyperefContext

        def typeref(self):
            return self.getTypedRuleContext(CprestoParser.TyperefContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_typename

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypename" ):
                listener.enterTypename(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypename" ):
                listener.exitTypename(self)




    def typename(self):

        localctx = CprestoParser.TypenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_typename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            localctx.ref = self.typeref()

            localctx.res = TypeNode(localctx.ref.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyperefContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.ref = None # Typeref_baseContext
            self.t = None # Token
            self.pms = None # Param_typerefsContext

        def typeref_base(self):
            return self.getTypedRuleContext(CprestoParser.Typeref_baseContext,0)


        def INTEGER(self, i:int=None):
            if i is None:
                return self.getTokens(CprestoParser.INTEGER)
            else:
                return self.getToken(CprestoParser.INTEGER, i)

        def param_typerefs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Param_typerefsContext)
            else:
                return self.getTypedRuleContext(CprestoParser.Param_typerefsContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_typeref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyperef" ):
                listener.enterTyperef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyperef" ):
                listener.exitTyperef(self)




    def typeref(self):

        localctx = CprestoParser.TyperefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_typeref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            localctx.ref = self.typeref_base()
            self.state = 340
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__2) | (1 << CprestoParser.T__9) | (1 << CprestoParser.T__11))) != 0):
                self.state = 338
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 324
                    self.match(CprestoParser.T__9)
                    self.state = 325
                    self.match(CprestoParser.T__10)

                    localctx.ref.res = ArrayTypeRef(localctx.ref.res)

                    pass

                elif la_ == 2:
                    self.state = 327
                    self.match(CprestoParser.T__9)
                    self.state = 328
                    localctx.t = self.match(CprestoParser.INTEGER)
                    self.state = 329
                    self.match(CprestoParser.T__10)

                    localctx.ref.res = ArrayTypeRef(localctx.ref.res,self.integer_value((None if localctx.t is None else localctx.t.text)))

                    pass

                elif la_ == 3:
                    self.state = 331
                    self.match(CprestoParser.T__11)

                    localctx.ref.res = PointerTypeRef(localctx.ref.res)

                    pass

                elif la_ == 4:
                    self.state = 333
                    self.match(CprestoParser.T__2)
                    self.state = 334
                    localctx.pms = self.param_typerefs()
                    self.state = 335
                    self.match(CprestoParser.T__3)

                    localctx.ref.res = FunctionTypeRef(localctx.ref.res,pms)

                    pass


                self.state = 342
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.ref.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_typerefsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.pms = None # Fixedparam_typerefsContext

        def VOID(self):
            return self.getToken(CprestoParser.VOID, 0)

        def fixedparam_typerefs(self):
            return self.getTypedRuleContext(CprestoParser.Fixedparam_typerefsContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_param_typerefs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam_typerefs" ):
                listener.enterParam_typerefs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam_typerefs" ):
                listener.exitParam_typerefs(self)




    def param_typerefs(self):

        localctx = CprestoParser.Param_typerefsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param_typerefs)
        self._la = 0 # Token type
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.match(CprestoParser.VOID)

                localctx.res = ParamTypeRefs([])

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 347
                localctx.pms = self.fixedparam_typerefs()
                self.state = 351
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CprestoParser.T__5:
                    self.state = 348
                    self.match(CprestoParser.T__5)
                    self.state = 349
                    self.match(CprestoParser.T__6)

                    localctx.pms.res.accept_varargs()




                localctx.res = localctx.pms.res

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fixedparam_typerefsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.tmp = list()
            self.ref = None # TyperefContext

        def typeref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.TyperefContext)
            else:
                return self.getTypedRuleContext(CprestoParser.TyperefContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_fixedparam_typerefs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixedparam_typerefs" ):
                listener.enterFixedparam_typerefs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixedparam_typerefs" ):
                listener.exitFixedparam_typerefs(self)




    def fixedparam_typerefs(self):

        localctx = CprestoParser.Fixedparam_typerefsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_fixedparam_typerefs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            localctx.ref = self.typeref()

            localctx.tmp.append(localctx.ref.res)

            self.state = 365
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 359
                    self.match(CprestoParser.T__5)
                    self.state = 360
                    localctx.ref = self.typeref()

                    if localctx.ref != None:
                            localctx.tmp.append(localctx.ref.res)
             
                self.state = 367
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)


            localctx.res = ParamTypeRefs(localctx.tmp)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Typeref_baseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.i = None # Token

        def CHAR(self):
            return self.getToken(CprestoParser.CHAR, 0)

        def SHORT(self):
            return self.getToken(CprestoParser.SHORT, 0)

        def INT(self):
            return self.getToken(CprestoParser.INT, 0)

        def LONG(self):
            return self.getToken(CprestoParser.LONG, 0)

        def VOID(self):
            return self.getToken(CprestoParser.VOID, 0)

        def UNSIGNED(self):
            return self.getToken(CprestoParser.UNSIGNED, 0)

        def STRUCT(self):
            return self.getToken(CprestoParser.STRUCT, 0)

        def IDENTIFIER(self):
            return self.getToken(CprestoParser.IDENTIFIER, 0)

        def UNION(self):
            return self.getToken(CprestoParser.UNION, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_typeref_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyperef_base" ):
                listener.enterTyperef_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyperef_base" ):
                listener.exitTyperef_base(self)




    def typeref_base(self):

        localctx = CprestoParser.Typeref_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_typeref_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 370
                localctx.t = self.match(CprestoParser.VOID)

                localctx.res = VoidTypeRef(self.location(localctx.t))

                pass

            elif la_ == 2:
                self.state = 372
                localctx.t = self.match(CprestoParser.CHAR)

                localctx.res = IntegerTypeRef.char_ref(self.location(localctx.t))

                pass

            elif la_ == 3:
                self.state = 374
                localctx.t = self.match(CprestoParser.SHORT)

                localctx.res = IntegerTypeRef.short_ref(self.location(localctx.t))

                pass

            elif la_ == 4:
                self.state = 376
                localctx.t = self.match(CprestoParser.INT)

                localctx.res = IntegerTypeRef.int_ref(self.location(localctx.t))

                pass

            elif la_ == 5:
                self.state = 378
                localctx.t = self.match(CprestoParser.LONG)

                localctx.res = IntegerTypeRef.long_ref(self.location(localctx.t))

                pass

            elif la_ == 6:
                self.state = 380
                localctx.t = self.match(CprestoParser.UNSIGNED)
                self.state = 381
                self.match(CprestoParser.CHAR)

                localctx.res = IntegerTypeRef.uchar_ref(self.location(localctx.t))

                pass

            elif la_ == 7:
                self.state = 383
                localctx.t = self.match(CprestoParser.UNSIGNED)
                self.state = 384
                self.match(CprestoParser.SHORT)

                localctx.res = IntegerTypeRef.ushort_ref(self.location(localctx.t))

                pass

            elif la_ == 8:
                self.state = 386
                localctx.t = self.match(CprestoParser.UNSIGNED)
                self.state = 387
                self.match(CprestoParser.INT)

                localctx.res = IntegerTypeRef.uint_ref(self.location(localctx.t))

                pass

            elif la_ == 9:
                self.state = 389
                localctx.t = self.match(CprestoParser.UNSIGNED)
                self.state = 390
                self.match(CprestoParser.LONG)

                localctx.res = IntegerTypeRef.ulong_ref(self.location(localctx.t))

                pass

            elif la_ == 10:
                self.state = 392
                localctx.t = self.match(CprestoParser.STRUCT)
                self.state = 393
                localctx.i = self.match(CprestoParser.IDENTIFIER)

                localctx.res = StructTypeRef((None if localctx.i is None else localctx.i.text),self.location(localctx.t))

                pass

            elif la_ == 11:
                self.state = 395
                localctx.t = self.match(CprestoParser.UNION)
                self.state = 396
                localctx.i = self.match(CprestoParser.IDENTIFIER)

                localctx.res = UnionTypeRef((None if localctx.i is None else localctx.i.text),self.location(localctx.t))

                pass

            elif la_ == 12:
                self.state = 398
                if not self.is_type(self._input.LT(1).text):
                    from antlr4.error.Errors import FailedPredicateException
                    raise FailedPredicateException(self, "self.is_type(self._input.LT(1).text)")
                self.state = 399
                localctx.i = self.match(CprestoParser.IDENTIFIER)

                localctx.res = UserTypeRef((None if localctx.i is None else localctx.i.text),self.location(localctx.t))

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.ss = list()
            self.s = None # StmtContext

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.StmtContext)
            else:
                return self.getTypedRuleContext(CprestoParser.StmtContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)




    def stmts(self):

        localctx = CprestoParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__1) | (1 << CprestoParser.T__2) | (1 << CprestoParser.T__7) | (1 << CprestoParser.T__11) | (1 << CprestoParser.T__34) | (1 << CprestoParser.T__37) | (1 << CprestoParser.T__38) | (1 << CprestoParser.T__41) | (1 << CprestoParser.T__42) | (1 << CprestoParser.T__43) | (1 << CprestoParser.T__44) | (1 << CprestoParser.IF) | (1 << CprestoParser.SWITCH))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CprestoParser.WHILE - 65)) | (1 << (CprestoParser.DO - 65)) | (1 << (CprestoParser.FOR - 65)) | (1 << (CprestoParser.RETURN - 65)) | (1 << (CprestoParser.BREAK - 65)) | (1 << (CprestoParser.CONTINUE - 65)) | (1 << (CprestoParser.GOTO - 65)) | (1 << (CprestoParser.SIZEOF - 65)) | (1 << (CprestoParser.IDENTIFIER - 65)) | (1 << (CprestoParser.INTEGER - 65)) | (1 << (CprestoParser.STRING - 65)) | (1 << (CprestoParser.CHARACTER - 65)))) != 0):
                self.state = 403
                localctx.s = self.stmt()

                if localctx.s != None: 
                        localctx.ss.append(localctx.s.res) 

                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.ss

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.n = None # Labeled_stmtContext
            self.e = None # ExprContext
            self.n1 = None # BlockContext
            self.n2 = None # If_stmtContext
            self.n3 = None # While_stmtContext
            self.n4 = None # Dowhile_stmtContext
            self.n5 = None # For_stmtContext
            self.n6 = None # Switch_stmtContext
            self.n7 = None # Break_stmtContext
            self.n8 = None # Continue_stmtContext
            self.n9 = None # Goto_stmtContext
            self.n10 = None # Return_stmtContext

        def labeled_stmt(self):
            return self.getTypedRuleContext(CprestoParser.Labeled_stmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(CprestoParser.BlockContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(CprestoParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(CprestoParser.While_stmtContext,0)


        def dowhile_stmt(self):
            return self.getTypedRuleContext(CprestoParser.Dowhile_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(CprestoParser.For_stmtContext,0)


        def switch_stmt(self):
            return self.getTypedRuleContext(CprestoParser.Switch_stmtContext,0)


        def break_stmt(self):
            return self.getTypedRuleContext(CprestoParser.Break_stmtContext,0)


        def continue_stmt(self):
            return self.getTypedRuleContext(CprestoParser.Continue_stmtContext,0)


        def goto_stmt(self):
            return self.getTypedRuleContext(CprestoParser.Goto_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(CprestoParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = CprestoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 413
                self.match(CprestoParser.T__1)

                localctx.res = None

                pass

            elif la_ == 2:
                self.state = 415
                localctx.n = self.labeled_stmt()

                localctx.res = localctx.n.res

                pass

            elif la_ == 3:
                self.state = 418
                localctx.e = self.expr()
                self.state = 419
                self.match(CprestoParser.T__1)

                localctx.res = ExprStmtNode(localctx.e.res.location(),localctx.e.res)

                pass

            elif la_ == 4:
                self.state = 422
                localctx.n1 = self.block()

                localctx.res = localctx.n1.res

                pass

            elif la_ == 5:
                self.state = 425
                localctx.n2 = self.if_stmt()

                localctx.res = localctx.n2.res

                pass

            elif la_ == 6:
                self.state = 428
                localctx.n3 = self.while_stmt()

                localctx.res = localctx.n3.res

                pass

            elif la_ == 7:
                self.state = 431
                localctx.n4 = self.dowhile_stmt()

                localctx.res = localctx.n4.res

                pass

            elif la_ == 8:
                self.state = 434
                localctx.n5 = self.for_stmt()

                localctx.res = localctx.n5.res

                pass

            elif la_ == 9:
                self.state = 437
                localctx.n6 = self.switch_stmt()

                localctx.res = localctx.n6.res

                pass

            elif la_ == 10:
                self.state = 440
                localctx.n7 = self.break_stmt()

                localctx.res = localctx.n7.res

                pass

            elif la_ == 11:
                self.state = 443
                localctx.n8 = self.continue_stmt()

                localctx.res = localctx.n8.res

                pass

            elif la_ == 12:
                self.state = 446
                localctx.n9 = self.goto_stmt()

                localctx.res = localctx.n9.res

                pass

            elif la_ == 13:
                self.state = 449
                localctx.n10 = self.return_stmt()

                localctx.res = localctx.n10.res

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Labeled_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.n = None # StmtContext

        def IDENTIFIER(self):
            return self.getToken(CprestoParser.IDENTIFIER, 0)

        def stmt(self):
            return self.getTypedRuleContext(CprestoParser.StmtContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_labeled_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLabeled_stmt" ):
                listener.enterLabeled_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLabeled_stmt" ):
                listener.exitLabeled_stmt(self)




    def labeled_stmt(self):

        localctx = CprestoParser.Labeled_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_labeled_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 454
            localctx.t = self.match(CprestoParser.IDENTIFIER)
            self.state = 455
            self.match(CprestoParser.T__12)
            self.state = 456
            localctx.n = self.stmt()

            localctx.res = LabelNode(self.location(localctx.t), (None if localctx.t is None else localctx.t.text), localctx.n.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.cond = None # ExprContext
            self.thenbody = None # StmtContext
            self.elsebody = None # StmtContext

        def IF(self):
            return self.getToken(CprestoParser.IF, 0)

        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.StmtContext)
            else:
                return self.getTypedRuleContext(CprestoParser.StmtContext,i)


        def ELSE(self):
            return self.getToken(CprestoParser.ELSE, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_if_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_stmt" ):
                listener.enterIf_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_stmt" ):
                listener.exitIf_stmt(self)




    def if_stmt(self):

        localctx = CprestoParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_if_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 459
            localctx.t = self.match(CprestoParser.IF)
            self.state = 460
            self.match(CprestoParser.T__2)
            self.state = 461
            localctx.cond = self.expr()
            self.state = 462
            self.match(CprestoParser.T__3)
            self.state = 463
            localctx.thenbody = self.stmt()
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 464
                self.match(CprestoParser.ELSE)
                self.state = 465
                localctx.elsebody = self.stmt()



            localctx.res = IfNode(self.location(localctx.t),localctx.cond.res,localctx.thenbody.res,localctx.elsebody.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.cond = None # ExprContext
            self.body = None # StmtContext

        def WHILE(self):
            return self.getToken(CprestoParser.WHILE, 0)

        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def stmt(self):
            return self.getTypedRuleContext(CprestoParser.StmtContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_while_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stmt" ):
                listener.enterWhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stmt" ):
                listener.exitWhile_stmt(self)




    def while_stmt(self):

        localctx = CprestoParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            localctx.t = self.match(CprestoParser.WHILE)
            self.state = 471
            self.match(CprestoParser.T__2)
            self.state = 472
            localctx.cond = self.expr()
            self.state = 473
            self.match(CprestoParser.T__3)
            self.state = 474
            localctx.body = self.stmt()

            localctx.res = WhileNode(self.location(localctx.t),localctx.cond.res,localctx.body.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Dowhile_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.body = None # StmtContext
            self.cond = None # ExprContext

        def WHILE(self):
            return self.getToken(CprestoParser.WHILE, 0)

        def DO(self):
            return self.getToken(CprestoParser.DO, 0)

        def stmt(self):
            return self.getTypedRuleContext(CprestoParser.StmtContext,0)


        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_dowhile_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDowhile_stmt" ):
                listener.enterDowhile_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDowhile_stmt" ):
                listener.exitDowhile_stmt(self)




    def dowhile_stmt(self):

        localctx = CprestoParser.Dowhile_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_dowhile_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            localctx.t = self.match(CprestoParser.DO)
            self.state = 478
            localctx.body = self.stmt()
            self.state = 479
            self.match(CprestoParser.WHILE)
            self.state = 480
            self.match(CprestoParser.T__2)
            self.state = 481
            localctx.cond = self.expr()
            self.state = 482
            self.match(CprestoParser.T__3)
            self.state = 483
            self.match(CprestoParser.T__1)

            localctx.res = DoWhileNode(self.location(localctx.t),localctx.body.res,localctx.cond.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.ini = None # ExprContext
            self.co = None # ExprContext
            self.incr = None # ExprContext
            self.body = None # StmtContext

        def FOR(self):
            return self.getToken(CprestoParser.FOR, 0)

        def stmt(self):
            return self.getTypedRuleContext(CprestoParser.StmtContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.ExprContext)
            else:
                return self.getTypedRuleContext(CprestoParser.ExprContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_for_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor_stmt" ):
                listener.enterFor_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor_stmt" ):
                listener.exitFor_stmt(self)




    def for_stmt(self):

        localctx = CprestoParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            localctx.t = self.match(CprestoParser.FOR)
            self.state = 487
            self.match(CprestoParser.T__2)
            self.state = 489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__2) | (1 << CprestoParser.T__11) | (1 << CprestoParser.T__34) | (1 << CprestoParser.T__37) | (1 << CprestoParser.T__38) | (1 << CprestoParser.T__41) | (1 << CprestoParser.T__42) | (1 << CprestoParser.T__43) | (1 << CprestoParser.T__44))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CprestoParser.SIZEOF - 74)) | (1 << (CprestoParser.IDENTIFIER - 74)) | (1 << (CprestoParser.INTEGER - 74)) | (1 << (CprestoParser.STRING - 74)) | (1 << (CprestoParser.CHARACTER - 74)))) != 0):
                self.state = 488
                localctx.ini = self.expr()


            self.state = 491
            self.match(CprestoParser.T__1)
            self.state = 493
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__2) | (1 << CprestoParser.T__11) | (1 << CprestoParser.T__34) | (1 << CprestoParser.T__37) | (1 << CprestoParser.T__38) | (1 << CprestoParser.T__41) | (1 << CprestoParser.T__42) | (1 << CprestoParser.T__43) | (1 << CprestoParser.T__44))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CprestoParser.SIZEOF - 74)) | (1 << (CprestoParser.IDENTIFIER - 74)) | (1 << (CprestoParser.INTEGER - 74)) | (1 << (CprestoParser.STRING - 74)) | (1 << (CprestoParser.CHARACTER - 74)))) != 0):
                self.state = 492
                localctx.co = self.expr()


            self.state = 495
            self.match(CprestoParser.T__1)
            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__2) | (1 << CprestoParser.T__11) | (1 << CprestoParser.T__34) | (1 << CprestoParser.T__37) | (1 << CprestoParser.T__38) | (1 << CprestoParser.T__41) | (1 << CprestoParser.T__42) | (1 << CprestoParser.T__43) | (1 << CprestoParser.T__44))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CprestoParser.SIZEOF - 74)) | (1 << (CprestoParser.IDENTIFIER - 74)) | (1 << (CprestoParser.INTEGER - 74)) | (1 << (CprestoParser.STRING - 74)) | (1 << (CprestoParser.CHARACTER - 74)))) != 0):
                self.state = 496
                localctx.incr = self.expr()


            self.state = 499
            self.match(CprestoParser.T__3)
            self.state = 500
            localctx.body = self.stmt()

            localctx.res = ForNode(self.location(localctx.t),localctx.ini.res,localctx.co.res,localctx.incr.res,localctx.body.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.cond = None # ExprContext
            self.bodies = None # Case_clausesContext

        def SWITCH(self):
            return self.getToken(CprestoParser.SWITCH, 0)

        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def case_clauses(self):
            return self.getTypedRuleContext(CprestoParser.Case_clausesContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_switch_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch_stmt" ):
                listener.enterSwitch_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch_stmt" ):
                listener.exitSwitch_stmt(self)




    def switch_stmt(self):

        localctx = CprestoParser.Switch_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 503
            localctx.t = self.match(CprestoParser.SWITCH)
            self.state = 504
            self.match(CprestoParser.T__2)
            self.state = 505
            localctx.cond = self.expr()
            self.state = 506
            self.match(CprestoParser.T__3)
            self.state = 507
            self.match(CprestoParser.T__7)
            self.state = 508
            localctx.bodies = self.case_clauses()
            self.state = 509
            self.match(CprestoParser.T__8)

            localctx.res = SwitchNode(self.location(localctx.t),localctx.cond.res,localctx.bodies.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_clausesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.cls = list()
            self.n = None # Case_clauseContext
            self.d = None # Default_clauseContext

        def case_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Case_clauseContext)
            else:
                return self.getTypedRuleContext(CprestoParser.Case_clauseContext,i)


        def default_clause(self):
            return self.getTypedRuleContext(CprestoParser.Default_clauseContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_case_clauses

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_clauses" ):
                listener.enterCase_clauses(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_clauses" ):
                listener.exitCase_clauses(self)




    def case_clauses(self):

        localctx = CprestoParser.Case_clausesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_case_clauses)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.CASE:
                self.state = 512
                localctx.n = self.case_clause()

                localctx.cls.append(localctx.n.res)

                self.state = 519
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CprestoParser.DEFAULT:
                self.state = 520
                localctx.d = self.default_clause()

                if localctx.d != None:
                        localctx.cls.append(localctx.d.res)




            localctx.res = localctx.cls

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.values = None # CasesContext
            self.body = None # Case_bodyContext

        def cases(self):
            return self.getTypedRuleContext(CprestoParser.CasesContext,0)


        def case_body(self):
            return self.getTypedRuleContext(CprestoParser.Case_bodyContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_case_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_clause" ):
                listener.enterCase_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_clause" ):
                listener.exitCase_clause(self)




    def case_clause(self):

        localctx = CprestoParser.Case_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_case_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 527
            localctx.values = self.cases()
            self.state = 528
            localctx.body = self.case_body()

            localctx.res = CaseNode(localctx.body.res.location(),localctx.values.res,localctx.body.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CasesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.values = list()
            self.n = None # PrimaryContext

        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(CprestoParser.CASE)
            else:
                return self.getToken(CprestoParser.CASE, i)

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(CprestoParser.PrimaryContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_cases

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCases" ):
                listener.enterCases(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCases" ):
                listener.exitCases(self)




    def cases(self):

        localctx = CprestoParser.CasesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_cases)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 531
                self.match(CprestoParser.CASE)
                self.state = 532
                localctx.n = self.primary()
                self.state = 533
                self.match(CprestoParser.T__12)

                localctx.values.append(localctx.n.res)

                self.state = 538 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==CprestoParser.CASE):
                    break


            localctx.res = localctx.values

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.body = None # Case_bodyContext

        def DEFAULT(self):
            return self.getToken(CprestoParser.DEFAULT, 0)

        def case_body(self):
            return self.getTypedRuleContext(CprestoParser.Case_bodyContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_default_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefault_clause" ):
                listener.enterDefault_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefault_clause" ):
                listener.exitDefault_clause(self)




    def default_clause(self):

        localctx = CprestoParser.Default_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_default_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(CprestoParser.DEFAULT)
            self.state = 543
            self.match(CprestoParser.T__12)
            self.state = 544
            localctx.body = self.case_body()

            localctx.res = CaseNode(localctx.body.res.location(),[],localctx.body.res)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_bodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.sts = list()
            self.s = None # StmtContext

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.StmtContext)
            else:
                return self.getTypedRuleContext(CprestoParser.StmtContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_case_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCase_body" ):
                listener.enterCase_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCase_body" ):
                listener.exitCase_body(self)




    def case_body(self):

        localctx = CprestoParser.Case_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_case_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 550 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 547
                localctx.s = self.stmt()

                if localctx.s != None:
                        localctx.sts.append(localctx.s.res)

                self.state = 552 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__1) | (1 << CprestoParser.T__2) | (1 << CprestoParser.T__7) | (1 << CprestoParser.T__11) | (1 << CprestoParser.T__34) | (1 << CprestoParser.T__37) | (1 << CprestoParser.T__38) | (1 << CprestoParser.T__41) | (1 << CprestoParser.T__42) | (1 << CprestoParser.T__43) | (1 << CprestoParser.T__44) | (1 << CprestoParser.IF) | (1 << CprestoParser.SWITCH))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (CprestoParser.WHILE - 65)) | (1 << (CprestoParser.DO - 65)) | (1 << (CprestoParser.FOR - 65)) | (1 << (CprestoParser.RETURN - 65)) | (1 << (CprestoParser.BREAK - 65)) | (1 << (CprestoParser.CONTINUE - 65)) | (1 << (CprestoParser.GOTO - 65)) | (1 << (CprestoParser.SIZEOF - 65)) | (1 << (CprestoParser.IDENTIFIER - 65)) | (1 << (CprestoParser.INTEGER - 65)) | (1 << (CprestoParser.STRING - 65)) | (1 << (CprestoParser.CHARACTER - 65)))) != 0)):
                    break


            if not isinstance(localctx.sts[-1],BreakNode):
                    raise ParseException('missing break statement at the last of case clause')
            localctx.res = BlockNode(localctx.sts[0].location(),[],localctx.sts)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token

        def BREAK(self):
            return self.getToken(CprestoParser.BREAK, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_break_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_stmt" ):
                listener.enterBreak_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_stmt" ):
                listener.exitBreak_stmt(self)




    def break_stmt(self):

        localctx = CprestoParser.Break_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_break_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            localctx.t = self.match(CprestoParser.BREAK)
            self.state = 557
            self.match(CprestoParser.T__1)

            localctx.res = BreakNode(self.location(localctx.t))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token

        def CONTINUE(self):
            return self.getToken(CprestoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_continue_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_stmt" ):
                listener.enterContinue_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_stmt" ):
                listener.exitContinue_stmt(self)




    def continue_stmt(self):

        localctx = CprestoParser.Continue_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_continue_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            localctx.t = self.match(CprestoParser.CONTINUE)
            self.state = 561
            self.match(CprestoParser.T__1)

            localctx.res = ContinueNode(self.location(localctx.t))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Goto_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.n = None # Token

        def GOTO(self):
            return self.getToken(CprestoParser.GOTO, 0)

        def IDENTIFIER(self):
            return self.getToken(CprestoParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CprestoParser.RULE_goto_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoto_stmt" ):
                listener.enterGoto_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoto_stmt" ):
                listener.exitGoto_stmt(self)




    def goto_stmt(self):

        localctx = CprestoParser.Goto_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_goto_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 564
            localctx.t = self.match(CprestoParser.GOTO)
            self.state = 565
            localctx.n = self.match(CprestoParser.IDENTIFIER)
            self.state = 566
            self.match(CprestoParser.T__1)

            localctx.res = GotoNode(self.location(localctx.t),(None if localctx.n is None else localctx.n.text))

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.exp = None # ExprContext

        def RETURN(self):
            return self.getToken(CprestoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_return_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stmt" ):
                listener.enterReturn_stmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stmt" ):
                listener.exitReturn_stmt(self)




    def return_stmt(self):

        localctx = CprestoParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_return_stmt)
        try:
            self.state = 577
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 569
                localctx.t = self.match(CprestoParser.RETURN)
                self.state = 570
                self.match(CprestoParser.T__1)

                localctx.res = ReturnNode(self.location(localctx.t),None)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 572
                localctx.t = self.match(CprestoParser.RETURN)
                self.state = 573
                localctx.exp = self.expr()
                self.state = 574
                self.match(CprestoParser.T__1)

                localctx.res = ReturnNode(self.location(localctx.t),localctx.exp.res)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.lhs = None # TermContext
            self.rhs = None # ExprContext
            self.op = None # Opassign_opContext
            self.e = None # Expr10Context

        def term(self):
            return self.getTypedRuleContext(CprestoParser.TermContext,0)


        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def opassign_op(self):
            return self.getTypedRuleContext(CprestoParser.Opassign_opContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CprestoParser.Expr10Context,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = CprestoParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr)
        try:
            self.state = 592
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 579
                localctx.lhs = self.term()
                self.state = 580
                self.match(CprestoParser.T__4)
                self.state = 581
                localctx.rhs = self.expr()

                localctx.res = AssignNode(localctx.lhs.res,localctx.rhs.res)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 584
                localctx.lhs = self.term()
                self.state = 585
                localctx.op = self.opassign_op()
                self.state = 586
                localctx.rhs = self.expr()

                localctx.res = OpAssignNode(localctx.lhs.res,localctx.op.res,localctx.rhs.res)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 589
                localctx.e = self.expr10()

                localctx.res = localctx.e.res

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opassign_opContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None


        def getRuleIndex(self):
            return CprestoParser.RULE_opassign_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpassign_op" ):
                listener.enterOpassign_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpassign_op" ):
                listener.exitOpassign_op(self)




    def opassign_op(self):

        localctx = CprestoParser.Opassign_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_opassign_op)
        try:
            self.state = 614
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CprestoParser.T__13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 594
                self.match(CprestoParser.T__13)

                localctx.res = '+'

                pass
            elif token in [CprestoParser.T__14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 596
                self.match(CprestoParser.T__14)

                localctx.res = '-'

                pass
            elif token in [CprestoParser.T__15]:
                self.enterOuterAlt(localctx, 3)
                self.state = 598
                self.match(CprestoParser.T__15)

                localctx.res = '*'

                pass
            elif token in [CprestoParser.T__16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 600
                self.match(CprestoParser.T__16)

                localctx.res = '/'

                pass
            elif token in [CprestoParser.T__17]:
                self.enterOuterAlt(localctx, 5)
                self.state = 602
                self.match(CprestoParser.T__17)

                localctx.res = '%'

                pass
            elif token in [CprestoParser.T__18]:
                self.enterOuterAlt(localctx, 6)
                self.state = 604
                self.match(CprestoParser.T__18)

                localctx.res = '&'

                pass
            elif token in [CprestoParser.T__19]:
                self.enterOuterAlt(localctx, 7)
                self.state = 606
                self.match(CprestoParser.T__19)

                localctx.res = '|'

                pass
            elif token in [CprestoParser.T__20]:
                self.enterOuterAlt(localctx, 8)
                self.state = 608
                self.match(CprestoParser.T__20)

                localctx.res = '^'

                pass
            elif token in [CprestoParser.T__21]:
                self.enterOuterAlt(localctx, 9)
                self.state = 610
                self.match(CprestoParser.T__21)

                localctx.res = '<<'

                pass
            elif token in [CprestoParser.T__22]:
                self.enterOuterAlt(localctx, 10)
                self.state = 612
                self.match(CprestoParser.T__22)

                localctx.res = '>>'

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr10Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.c = None # Expr9Context
            self.t = None # ExprContext
            self.e = None # Expr10Context

        def expr9(self):
            return self.getTypedRuleContext(CprestoParser.Expr9Context,0)


        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def expr10(self):
            return self.getTypedRuleContext(CprestoParser.Expr10Context,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr10

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr10" ):
                listener.enterExpr10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr10" ):
                listener.exitExpr10(self)




    def expr10(self):

        localctx = CprestoParser.Expr10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expr10)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 616
            localctx.c = self.expr9()

            localctx.res = localctx.c.res

            self.state = 624
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==CprestoParser.T__23:
                self.state = 618
                self.match(CprestoParser.T__23)
                self.state = 619
                localctx.t = self.expr()
                self.state = 620
                self.match(CprestoParser.T__12)
                self.state = 621
                localctx.e = self.expr10()

                if localctx.t != None and localctx.e != None:
                        localctx.res = CondExprNode(localctx.c.res,localctx.t.res,localctx.e.res)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr8Context
            self.r = None # Expr8Context

        def expr8(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr8Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr8Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr9

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr9" ):
                listener.enterExpr9(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr9" ):
                listener.exitExpr9(self)




    def expr9(self):

        localctx = CprestoParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expr9)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            localctx.l = self.expr8()
            self.state = 633
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__24:
                self.state = 627
                self.match(CprestoParser.T__24)
                self.state = 628
                localctx.r = self.expr8()

                localctx.l.res = LogicalOrNode(localctx.l.res,localctx.r.res)

                self.state = 635
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr8Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr7Context
            self.r = None # Expr7Context

        def expr7(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr7Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr7Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr8

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr8" ):
                listener.enterExpr8(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr8" ):
                listener.exitExpr8(self)




    def expr8(self):

        localctx = CprestoParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 638
            localctx.l = self.expr7()
            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__25:
                self.state = 639
                self.match(CprestoParser.T__25)
                self.state = 640
                localctx.r = self.expr7()

                localctx.l.res = LogicalAndNode(localctx.l.res,localctx.r.res)

                self.state = 647
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr6Context
            self.r = None # Expr6Context

        def expr6(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr6Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr6Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr7

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr7" ):
                listener.enterExpr7(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr7" ):
                listener.exitExpr7(self)




    def expr7(self):

        localctx = CprestoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_expr7)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            localctx.l = self.expr6()
            self.state = 677
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__26) | (1 << CprestoParser.T__27) | (1 << CprestoParser.T__28) | (1 << CprestoParser.T__29) | (1 << CprestoParser.T__30) | (1 << CprestoParser.T__31))) != 0):
                self.state = 675
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CprestoParser.T__26]:
                    self.state = 651
                    self.match(CprestoParser.T__26)
                    self.state = 652
                    localctx.r = self.expr6()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'>',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__27]:
                    self.state = 655
                    self.match(CprestoParser.T__27)
                    self.state = 656
                    localctx.r = self.expr6()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'<',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__28]:
                    self.state = 659
                    self.match(CprestoParser.T__28)
                    self.state = 660
                    localctx.r = self.expr6()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'>=',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__29]:
                    self.state = 663
                    self.match(CprestoParser.T__29)
                    self.state = 664
                    localctx.r = self.expr6()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'<=',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__30]:
                    self.state = 667
                    self.match(CprestoParser.T__30)
                    self.state = 668
                    localctx.r = self.expr6()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'==',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__31]:
                    self.state = 671
                    self.match(CprestoParser.T__31)
                    self.state = 672
                    localctx.r = self.expr6()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'!=',localctx.r.res)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 679
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr5Context
            self.r = None # Expr5Context

        def expr5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr5Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr5Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr6

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr6" ):
                listener.enterExpr6(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr6" ):
                listener.exitExpr6(self)




    def expr6(self):

        localctx = CprestoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_expr6)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 682
            localctx.l = self.expr5()
            self.state = 689
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__32:
                self.state = 683
                self.match(CprestoParser.T__32)
                self.state = 684
                localctx.r = self.expr5()

                localctx.l.res = BinaryOpNode(localctx.l.res,'|',localctx.r.res)

                self.state = 691
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr4Context
            self.r = None # Expr4Context

        def expr4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr4Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr4Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr5

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr5" ):
                listener.enterExpr5(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr5" ):
                listener.exitExpr5(self)




    def expr5(self):

        localctx = CprestoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 694
            localctx.l = self.expr4()
            self.state = 701
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__33:
                self.state = 695
                self.match(CprestoParser.T__33)
                self.state = 696
                localctx.r = self.expr4()

                localctx.l.res = BinaryOpNode(localctx.l.res,'^',localctx.r.res)

                self.state = 703
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr3Context
            self.r = None # Expr3Context

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr3Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr3Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr4

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr4" ):
                listener.enterExpr4(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr4" ):
                listener.exitExpr4(self)




    def expr4(self):

        localctx = CprestoParser.Expr4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_expr4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 706
            localctx.l = self.expr3()
            self.state = 713
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__34:
                self.state = 707
                self.match(CprestoParser.T__34)
                self.state = 708
                localctx.r = self.expr3()

                localctx.l.res = BinaryOpNode(localctx.l.res,'&',localctx.r.res)

                self.state = 715
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr2Context
            self.r = None # Expr2Context

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr2Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr2Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr3

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr3" ):
                listener.enterExpr3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr3" ):
                listener.exitExpr3(self)




    def expr3(self):

        localctx = CprestoParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_expr3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 718
            localctx.l = self.expr2()
            self.state = 729
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__35 or _la==CprestoParser.T__36:
                self.state = 727
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CprestoParser.T__35]:
                    self.state = 719
                    self.match(CprestoParser.T__35)
                    self.state = 720
                    localctx.r = self.expr2()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'>>',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__36]:
                    self.state = 723
                    self.match(CprestoParser.T__36)
                    self.state = 724
                    localctx.r = self.expr2()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'<<',localctx.r.res)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 731
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # Expr1Context
            self.r = None # Expr1Context

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.Expr1Context)
            else:
                return self.getTypedRuleContext(CprestoParser.Expr1Context,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr2" ):
                listener.enterExpr2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr2" ):
                listener.exitExpr2(self)




    def expr2(self):

        localctx = CprestoParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_expr2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 734
            localctx.l = self.expr1()
            self.state = 745
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CprestoParser.T__37 or _la==CprestoParser.T__38:
                self.state = 743
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CprestoParser.T__37]:
                    self.state = 735
                    self.match(CprestoParser.T__37)
                    self.state = 736
                    localctx.r = self.expr1()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'+',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__38]:
                    self.state = 739
                    self.match(CprestoParser.T__38)
                    self.state = 740
                    localctx.r = self.expr1()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'-',localctx.r.res)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 747
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.l = None # TermContext
            self.r = None # TermContext

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.TermContext)
            else:
                return self.getTypedRuleContext(CprestoParser.TermContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_expr1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr1" ):
                listener.enterExpr1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr1" ):
                listener.exitExpr1(self)




    def expr1(self):

        localctx = CprestoParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_expr1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 750
            localctx.l = self.term()
            self.state = 765
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__11) | (1 << CprestoParser.T__39) | (1 << CprestoParser.T__40))) != 0):
                self.state = 763
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CprestoParser.T__11]:
                    self.state = 751
                    self.match(CprestoParser.T__11)
                    self.state = 752
                    localctx.r = self.term()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'*',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__39]:
                    self.state = 755
                    self.match(CprestoParser.T__39)
                    self.state = 756
                    localctx.r = self.term()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'/',localctx.r.res)

                    pass
                elif token in [CprestoParser.T__40]:
                    self.state = 759
                    self.match(CprestoParser.T__40)
                    self.state = 760
                    localctx.r = self.term()

                    localctx.l.res = BinaryOpNode(localctx.l.res,'%',localctx.r.res)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 767
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.l.res

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # TypenameContext
            self.n = None # TermContext
            self.u = None # UnaryContext

        def typename(self):
            return self.getTypedRuleContext(CprestoParser.TypenameContext,0)


        def term(self):
            return self.getTypedRuleContext(CprestoParser.TermContext,0)


        def unary(self):
            return self.getTypedRuleContext(CprestoParser.UnaryContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)




    def term(self):

        localctx = CprestoParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_term)
        try:
            self.state = 779
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 770
                self.match(CprestoParser.T__2)
                self.state = 771
                localctx.t = self.typename()
                self.state = 772
                self.match(CprestoParser.T__3)
                self.state = 773
                localctx.n = self.term()

                localctx.res = CastNode(localctx.t.res,localctx.n.res)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 776
                localctx.u = self.unary()

                localctx.res = localctx.u.res

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.n = None # UnaryContext
            self.m = None # TermContext
            self.t = None # TypenameContext
            self.p = None # PostfixContext

        def unary(self):
            return self.getTypedRuleContext(CprestoParser.UnaryContext,0)


        def term(self):
            return self.getTypedRuleContext(CprestoParser.TermContext,0)


        def SIZEOF(self):
            return self.getToken(CprestoParser.SIZEOF, 0)

        def typename(self):
            return self.getTypedRuleContext(CprestoParser.TypenameContext,0)


        def postfix(self):
            return self.getTypedRuleContext(CprestoParser.PostfixContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)




    def unary(self):

        localctx = CprestoParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_unary)
        try:
            self.state = 826
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 781
                self.match(CprestoParser.T__41)
                self.state = 782
                localctx.n = self.unary()

                localctx.res = PrefixOpNode('++',localctx.n.res)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 785
                self.match(CprestoParser.T__42)
                self.state = 786
                localctx.n = self.unary()

                localctx.res = PrefixOpNode('--',localctx.n.res)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 789
                self.match(CprestoParser.T__37)
                self.state = 790
                localctx.m = self.term()

                localctx.res = UnaryOpNode('+',localctx.m.res)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 793
                self.match(CprestoParser.T__38)
                self.state = 794
                localctx.m = self.term()

                localctx.res = UnaryOpNode('-',localctx.m.res)

                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 797
                self.match(CprestoParser.T__43)
                self.state = 798
                localctx.m = self.term()

                localctx.res = UnaryOpNode('!',localctx.m.res)

                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 801
                self.match(CprestoParser.T__44)
                self.state = 802
                localctx.m = self.term()

                localctx.res = UnaryOpNode('~',localctx.m.res)

                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 805
                self.match(CprestoParser.T__11)
                self.state = 806
                localctx.m = self.term()

                localctx.res = DereferenceNode(localctx.m.res)

                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 809
                self.match(CprestoParser.T__34)
                self.state = 810
                localctx.m = self.term()

                localctx.res = AddressNode(localctx.m.res)

                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 813
                self.match(CprestoParser.SIZEOF)
                self.state = 814
                self.match(CprestoParser.T__2)
                self.state = 815
                localctx.t = self.typename()
                self.state = 816
                self.match(CprestoParser.T__3)

                localctx.res = SizeofTypeNode(localctx.t.res,self.size_t())

                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 819
                self.match(CprestoParser.SIZEOF)
                self.state = 820
                localctx.n = self.unary()

                localctx.res = SizeofExprNode(localctx.n.res,self.size_t())

                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 823
                localctx.p = self.postfix()

                localctx.res = localctx.p.res

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PostfixContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.tmp = None
            self.e = None # PrimaryContext
            self.idx = None # ExprContext
            self.memb = None # NameContext
            self.ags = None # ArgsContext

        def primary(self):
            return self.getTypedRuleContext(CprestoParser.PrimaryContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.ExprContext)
            else:
                return self.getTypedRuleContext(CprestoParser.ExprContext,i)


        def name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.NameContext)
            else:
                return self.getTypedRuleContext(CprestoParser.NameContext,i)


        def args(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.ArgsContext)
            else:
                return self.getTypedRuleContext(CprestoParser.ArgsContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_postfix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostfix" ):
                listener.enterPostfix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostfix" ):
                listener.exitPostfix(self)




    def postfix(self):

        localctx = CprestoParser.PostfixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_postfix)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 828
            localctx.e = self.primary()

            localctx.tmp = localctx.e.res

            self.state = 854
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__0) | (1 << CprestoParser.T__2) | (1 << CprestoParser.T__9) | (1 << CprestoParser.T__41) | (1 << CprestoParser.T__42) | (1 << CprestoParser.T__45))) != 0):
                self.state = 852
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [CprestoParser.T__41]:
                    self.state = 830
                    self.match(CprestoParser.T__41)

                    localctx.tmp = SuffixOpNode('++',localctx.tmp)

                    pass
                elif token in [CprestoParser.T__42]:
                    self.state = 832
                    self.match(CprestoParser.T__42)

                    localctx.tmp = SuffixOpNode('--',localctx.tmp)

                    pass
                elif token in [CprestoParser.T__9]:
                    self.state = 834
                    self.match(CprestoParser.T__9)
                    self.state = 835
                    localctx.idx = self.expr()
                    self.state = 836
                    self.match(CprestoParser.T__10)

                    localctx.tmp = ArefNode(localctx.tmp,localctx.idx.res)

                    pass
                elif token in [CprestoParser.T__0]:
                    self.state = 839
                    self.match(CprestoParser.T__0)
                    self.state = 840
                    localctx.memb = self.name()

                    localctx.tmp = MemberNode(localctx.tmp,localctx.memb.res)

                    pass
                elif token in [CprestoParser.T__45]:
                    self.state = 843
                    self.match(CprestoParser.T__45)
                    self.state = 844
                    localctx.memb = self.name()

                    localctx.tmp = PtrMemberNode(localctx.tmp,localctx.memb.res)

                    pass
                elif token in [CprestoParser.T__2]:
                    self.state = 847
                    self.match(CprestoParser.T__2)
                    self.state = 848
                    localctx.ags = self.args()
                    self.state = 849
                    self.match(CprestoParser.T__3)

                    localctx.tmp = FuncallNode(localctx.tmp,localctx.ags.res)

                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 856
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.tmp

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.ags = list()
            self.arg = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.ExprContext)
            else:
                return self.getTypedRuleContext(CprestoParser.ExprContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_args

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgs" ):
                listener.enterArgs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgs" ):
                listener.exitArgs(self)




    def args(self):

        localctx = CprestoParser.ArgsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_args)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 870
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CprestoParser.T__2) | (1 << CprestoParser.T__11) | (1 << CprestoParser.T__34) | (1 << CprestoParser.T__37) | (1 << CprestoParser.T__38) | (1 << CprestoParser.T__41) | (1 << CprestoParser.T__42) | (1 << CprestoParser.T__43) | (1 << CprestoParser.T__44))) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & ((1 << (CprestoParser.SIZEOF - 74)) | (1 << (CprestoParser.IDENTIFIER - 74)) | (1 << (CprestoParser.INTEGER - 74)) | (1 << (CprestoParser.STRING - 74)) | (1 << (CprestoParser.CHARACTER - 74)))) != 0):
                self.state = 859
                localctx.arg = self.expr()

                localctx.ags.append(localctx.arg.res)

                self.state = 867
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==CprestoParser.T__5:
                    self.state = 861
                    self.match(CprestoParser.T__5)
                    self.state = 862
                    localctx.arg = self.expr()

                    localctx.ags.append(localctx.arg.res)

                    self.state = 869
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)




            localctx.res = localctx.ags

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None # Token
            self.e = None # ExprContext

        def INTEGER(self):
            return self.getToken(CprestoParser.INTEGER, 0)

        def CHARACTER(self):
            return self.getToken(CprestoParser.CHARACTER, 0)

        def STRING(self):
            return self.getToken(CprestoParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(CprestoParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(CprestoParser.ExprContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)




    def primary(self):

        localctx = CprestoParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_primary)
        try:
            self.state = 887
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CprestoParser.INTEGER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 874
                localctx.t = self.match(CprestoParser.INTEGER)

                localctx.res =  self.integer_node(self.location(localctx.t),(None if localctx.t is None else localctx.t.text))

                pass
            elif token in [CprestoParser.CHARACTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 876
                localctx.t = self.match(CprestoParser.CHARACTER)

                localctx.res =  IntegerLiteralNode(self.location(localctx.t),IntegerTypeRef.char_ref(),self.character_code((None if localctx.t is None else localctx.t.text)))

                pass
            elif token in [CprestoParser.STRING]:
                self.enterOuterAlt(localctx, 3)
                self.state = 878
                localctx.t = self.match(CprestoParser.STRING)

                localctx.res =  StringLiteralNode(self.location(localctx.t),PointerTypeRef(IntegerTypeRef.char_ref()),self.string_value((None if localctx.t is None else localctx.t.text)))

                pass
            elif token in [CprestoParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 4)
                self.state = 880
                localctx.t = self.match(CprestoParser.IDENTIFIER)

                localctx.res =  VariableNode(loc=self.location(localctx.t),name=(None if localctx.t is None else localctx.t.text))

                pass
            elif token in [CprestoParser.T__2]:
                self.enterOuterAlt(localctx, 5)
                self.state = 882
                self.match(CprestoParser.T__2)
                self.state = 883
                localctx.e = self.expr()
                self.state = 884
                self.match(CprestoParser.T__3)

                localctx.res = localctx.e.res

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Compilation_unitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.t = None
            self.impdecls = None # Import_stmtsContext
            self.decls = None # Top_defsContext

        def import_stmts(self):
            return self.getTypedRuleContext(CprestoParser.Import_stmtsContext,0)


        def top_defs(self):
            return self.getTypedRuleContext(CprestoParser.Top_defsContext,0)


        def getRuleIndex(self):
            return CprestoParser.RULE_compilation_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompilation_unit" ):
                listener.enterCompilation_unit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompilation_unit" ):
                listener.exitCompilation_unit(self)




    def compilation_unit(self):

        localctx = CprestoParser.Compilation_unitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_compilation_unit)
        try:
            self.enterOuterAlt(localctx, 1)

            print(self._input.LT(1).text)
            localctx.t = self._input.LT(1)

            self.state = 890
            localctx.impdecls = self.import_stmts()
            self.state = 891
            localctx.decls = self.top_defs()

            localctx.decls.res.add(localctx.impdecls.res)
            localctx.res=AST(self.location(localctx.t),localctx.decls.res) 

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Declaration_fileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.res = None
            self.decls = Declarations()
            self.impdecls = None # Import_stmtsContext
            self.fdecl = None # FuncdeclContext
            self.vdecl = None # VardeclContext
            self.defc = None # DefconstContext
            self.defs = None # DefstructContext
            self.defu = None # DefunionContext
            self.tdef = None # TypedefContext

        def import_stmts(self):
            return self.getTypedRuleContext(CprestoParser.Import_stmtsContext,0)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(CprestoParser.FuncdeclContext,i)


        def vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.VardeclContext)
            else:
                return self.getTypedRuleContext(CprestoParser.VardeclContext,i)


        def defconst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefconstContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefconstContext,i)


        def defstruct(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefstructContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefstructContext,i)


        def defunion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.DefunionContext)
            else:
                return self.getTypedRuleContext(CprestoParser.DefunionContext,i)


        def typedef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CprestoParser.TypedefContext)
            else:
                return self.getTypedRuleContext(CprestoParser.TypedefContext,i)


        def getRuleIndex(self):
            return CprestoParser.RULE_declaration_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration_file" ):
                listener.enterDeclaration_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration_file" ):
                listener.exitDeclaration_file(self)




    def declaration_file(self):

        localctx = CprestoParser.Declaration_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_declaration_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 894
            localctx.impdecls = self.import_stmts()
             
            localctx.decls.add(localctx.impdecls.res)

            self.state = 916
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 52)) & ~0x3f) == 0 and ((1 << (_la - 52)) & ((1 << (CprestoParser.STRUCT - 52)) | (1 << (CprestoParser.UNION - 52)) | (1 << (CprestoParser.EXTERN - 52)) | (1 << (CprestoParser.CONST - 52)) | (1 << (CprestoParser.TYPEDEF - 52)))) != 0):
                self.state = 914
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 896
                    localctx.fdecl = self.funcdecl()
                     
                    localctx.decls.add(localctx.fdecl.res)

                    pass

                elif la_ == 2:
                    self.state = 899
                    localctx.vdecl = self.vardecl()

                    localctx.decls.add(localctx.vdecl.res)

                    pass

                elif la_ == 3:
                    self.state = 902
                    localctx.defc = self.defconst()

                    localctx.decls.add(localctx.defc.res)

                    pass

                elif la_ == 4:
                    self.state = 905
                    localctx.defs = self.defstruct()

                    localctx.decls.add(localctx.defs.res)

                    pass

                elif la_ == 5:
                    self.state = 908
                    localctx.defu = self.defunion()

                    localctx.decls.add(localctx.defu.res)

                    pass

                elif la_ == 6:
                    self.state = 911
                    localctx.tdef = self.typedef()

                    localctx.decls.add(localctx.tdef.res)

                    pass


                self.state = 918
                self._errHandler.sync(self)
                _la = self._input.LA(1)


            localctx.res = localctx.decls

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.typeref_base_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def typeref_base_sempred(self, localctx:Typeref_baseContext, predIndex:int):
            if predIndex == 0:
                return self.is_type(self._input.LT(1).text)
         




