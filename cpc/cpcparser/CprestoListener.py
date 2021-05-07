# Generated from Cpresto.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CprestoParser import CprestoParser
else:
    from CprestoParser import CprestoParser

import sys
sys.path.append('../')

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



# This class defines a complete listener for a parse tree produced by CprestoParser.
class CprestoListener(ParseTreeListener):

    # Enter a parse tree produced by CprestoParser#import_stmts.
    def enterImport_stmts(self, ctx:CprestoParser.Import_stmtsContext):
        pass

    # Exit a parse tree produced by CprestoParser#import_stmts.
    def exitImport_stmts(self, ctx:CprestoParser.Import_stmtsContext):
        pass


    # Enter a parse tree produced by CprestoParser#import_stmt.
    def enterImport_stmt(self, ctx:CprestoParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#import_stmt.
    def exitImport_stmt(self, ctx:CprestoParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#funcdecl.
    def enterFuncdecl(self, ctx:CprestoParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by CprestoParser#funcdecl.
    def exitFuncdecl(self, ctx:CprestoParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by CprestoParser#vardecl.
    def enterVardecl(self, ctx:CprestoParser.VardeclContext):
        pass

    # Exit a parse tree produced by CprestoParser#vardecl.
    def exitVardecl(self, ctx:CprestoParser.VardeclContext):
        pass


    # Enter a parse tree produced by CprestoParser#name.
    def enterName(self, ctx:CprestoParser.NameContext):
        pass

    # Exit a parse tree produced by CprestoParser#name.
    def exitName(self, ctx:CprestoParser.NameContext):
        pass


    # Enter a parse tree produced by CprestoParser#top_defs.
    def enterTop_defs(self, ctx:CprestoParser.Top_defsContext):
        pass

    # Exit a parse tree produced by CprestoParser#top_defs.
    def exitTop_defs(self, ctx:CprestoParser.Top_defsContext):
        pass


    # Enter a parse tree produced by CprestoParser#defvars.
    def enterDefvars(self, ctx:CprestoParser.DefvarsContext):
        pass

    # Exit a parse tree produced by CprestoParser#defvars.
    def exitDefvars(self, ctx:CprestoParser.DefvarsContext):
        pass


    # Enter a parse tree produced by CprestoParser#storage.
    def enterStorage(self, ctx:CprestoParser.StorageContext):
        pass

    # Exit a parse tree produced by CprestoParser#storage.
    def exitStorage(self, ctx:CprestoParser.StorageContext):
        pass


    # Enter a parse tree produced by CprestoParser#defun.
    def enterDefun(self, ctx:CprestoParser.DefunContext):
        pass

    # Exit a parse tree produced by CprestoParser#defun.
    def exitDefun(self, ctx:CprestoParser.DefunContext):
        pass


    # Enter a parse tree produced by CprestoParser#params.
    def enterParams(self, ctx:CprestoParser.ParamsContext):
        pass

    # Exit a parse tree produced by CprestoParser#params.
    def exitParams(self, ctx:CprestoParser.ParamsContext):
        pass


    # Enter a parse tree produced by CprestoParser#fixedparams.
    def enterFixedparams(self, ctx:CprestoParser.FixedparamsContext):
        pass

    # Exit a parse tree produced by CprestoParser#fixedparams.
    def exitFixedparams(self, ctx:CprestoParser.FixedparamsContext):
        pass


    # Enter a parse tree produced by CprestoParser#param.
    def enterParam(self, ctx:CprestoParser.ParamContext):
        pass

    # Exit a parse tree produced by CprestoParser#param.
    def exitParam(self, ctx:CprestoParser.ParamContext):
        pass


    # Enter a parse tree produced by CprestoParser#block.
    def enterBlock(self, ctx:CprestoParser.BlockContext):
        pass

    # Exit a parse tree produced by CprestoParser#block.
    def exitBlock(self, ctx:CprestoParser.BlockContext):
        pass


    # Enter a parse tree produced by CprestoParser#defvar_list.
    def enterDefvar_list(self, ctx:CprestoParser.Defvar_listContext):
        pass

    # Exit a parse tree produced by CprestoParser#defvar_list.
    def exitDefvar_list(self, ctx:CprestoParser.Defvar_listContext):
        pass


    # Enter a parse tree produced by CprestoParser#defconst.
    def enterDefconst(self, ctx:CprestoParser.DefconstContext):
        pass

    # Exit a parse tree produced by CprestoParser#defconst.
    def exitDefconst(self, ctx:CprestoParser.DefconstContext):
        pass


    # Enter a parse tree produced by CprestoParser#defstruct.
    def enterDefstruct(self, ctx:CprestoParser.DefstructContext):
        pass

    # Exit a parse tree produced by CprestoParser#defstruct.
    def exitDefstruct(self, ctx:CprestoParser.DefstructContext):
        pass


    # Enter a parse tree produced by CprestoParser#defunion.
    def enterDefunion(self, ctx:CprestoParser.DefunionContext):
        pass

    # Exit a parse tree produced by CprestoParser#defunion.
    def exitDefunion(self, ctx:CprestoParser.DefunionContext):
        pass


    # Enter a parse tree produced by CprestoParser#member_list.
    def enterMember_list(self, ctx:CprestoParser.Member_listContext):
        pass

    # Exit a parse tree produced by CprestoParser#member_list.
    def exitMember_list(self, ctx:CprestoParser.Member_listContext):
        pass


    # Enter a parse tree produced by CprestoParser#slot.
    def enterSlot(self, ctx:CprestoParser.SlotContext):
        pass

    # Exit a parse tree produced by CprestoParser#slot.
    def exitSlot(self, ctx:CprestoParser.SlotContext):
        pass


    # Enter a parse tree produced by CprestoParser#typedef.
    def enterTypedef(self, ctx:CprestoParser.TypedefContext):
        pass

    # Exit a parse tree produced by CprestoParser#typedef.
    def exitTypedef(self, ctx:CprestoParser.TypedefContext):
        pass


    # Enter a parse tree produced by CprestoParser#typename.
    def enterTypename(self, ctx:CprestoParser.TypenameContext):
        pass

    # Exit a parse tree produced by CprestoParser#typename.
    def exitTypename(self, ctx:CprestoParser.TypenameContext):
        pass


    # Enter a parse tree produced by CprestoParser#typeref.
    def enterTyperef(self, ctx:CprestoParser.TyperefContext):
        pass

    # Exit a parse tree produced by CprestoParser#typeref.
    def exitTyperef(self, ctx:CprestoParser.TyperefContext):
        pass


    # Enter a parse tree produced by CprestoParser#param_typerefs.
    def enterParam_typerefs(self, ctx:CprestoParser.Param_typerefsContext):
        pass

    # Exit a parse tree produced by CprestoParser#param_typerefs.
    def exitParam_typerefs(self, ctx:CprestoParser.Param_typerefsContext):
        pass


    # Enter a parse tree produced by CprestoParser#fixedparam_typerefs.
    def enterFixedparam_typerefs(self, ctx:CprestoParser.Fixedparam_typerefsContext):
        pass

    # Exit a parse tree produced by CprestoParser#fixedparam_typerefs.
    def exitFixedparam_typerefs(self, ctx:CprestoParser.Fixedparam_typerefsContext):
        pass


    # Enter a parse tree produced by CprestoParser#typeref_base.
    def enterTyperef_base(self, ctx:CprestoParser.Typeref_baseContext):
        pass

    # Exit a parse tree produced by CprestoParser#typeref_base.
    def exitTyperef_base(self, ctx:CprestoParser.Typeref_baseContext):
        pass


    # Enter a parse tree produced by CprestoParser#stmts.
    def enterStmts(self, ctx:CprestoParser.StmtsContext):
        pass

    # Exit a parse tree produced by CprestoParser#stmts.
    def exitStmts(self, ctx:CprestoParser.StmtsContext):
        pass


    # Enter a parse tree produced by CprestoParser#stmt.
    def enterStmt(self, ctx:CprestoParser.StmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#stmt.
    def exitStmt(self, ctx:CprestoParser.StmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#labeled_stmt.
    def enterLabeled_stmt(self, ctx:CprestoParser.Labeled_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#labeled_stmt.
    def exitLabeled_stmt(self, ctx:CprestoParser.Labeled_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#if_stmt.
    def enterIf_stmt(self, ctx:CprestoParser.If_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#if_stmt.
    def exitIf_stmt(self, ctx:CprestoParser.If_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#while_stmt.
    def enterWhile_stmt(self, ctx:CprestoParser.While_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#while_stmt.
    def exitWhile_stmt(self, ctx:CprestoParser.While_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#dowhile_stmt.
    def enterDowhile_stmt(self, ctx:CprestoParser.Dowhile_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#dowhile_stmt.
    def exitDowhile_stmt(self, ctx:CprestoParser.Dowhile_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#for_stmt.
    def enterFor_stmt(self, ctx:CprestoParser.For_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#for_stmt.
    def exitFor_stmt(self, ctx:CprestoParser.For_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:CprestoParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:CprestoParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#case_clauses.
    def enterCase_clauses(self, ctx:CprestoParser.Case_clausesContext):
        pass

    # Exit a parse tree produced by CprestoParser#case_clauses.
    def exitCase_clauses(self, ctx:CprestoParser.Case_clausesContext):
        pass


    # Enter a parse tree produced by CprestoParser#case_clause.
    def enterCase_clause(self, ctx:CprestoParser.Case_clauseContext):
        pass

    # Exit a parse tree produced by CprestoParser#case_clause.
    def exitCase_clause(self, ctx:CprestoParser.Case_clauseContext):
        pass


    # Enter a parse tree produced by CprestoParser#cases.
    def enterCases(self, ctx:CprestoParser.CasesContext):
        pass

    # Exit a parse tree produced by CprestoParser#cases.
    def exitCases(self, ctx:CprestoParser.CasesContext):
        pass


    # Enter a parse tree produced by CprestoParser#default_clause.
    def enterDefault_clause(self, ctx:CprestoParser.Default_clauseContext):
        pass

    # Exit a parse tree produced by CprestoParser#default_clause.
    def exitDefault_clause(self, ctx:CprestoParser.Default_clauseContext):
        pass


    # Enter a parse tree produced by CprestoParser#case_body.
    def enterCase_body(self, ctx:CprestoParser.Case_bodyContext):
        pass

    # Exit a parse tree produced by CprestoParser#case_body.
    def exitCase_body(self, ctx:CprestoParser.Case_bodyContext):
        pass


    # Enter a parse tree produced by CprestoParser#break_stmt.
    def enterBreak_stmt(self, ctx:CprestoParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#break_stmt.
    def exitBreak_stmt(self, ctx:CprestoParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#continue_stmt.
    def enterContinue_stmt(self, ctx:CprestoParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#continue_stmt.
    def exitContinue_stmt(self, ctx:CprestoParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#goto_stmt.
    def enterGoto_stmt(self, ctx:CprestoParser.Goto_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#goto_stmt.
    def exitGoto_stmt(self, ctx:CprestoParser.Goto_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#return_stmt.
    def enterReturn_stmt(self, ctx:CprestoParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by CprestoParser#return_stmt.
    def exitReturn_stmt(self, ctx:CprestoParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by CprestoParser#expr.
    def enterExpr(self, ctx:CprestoParser.ExprContext):
        pass

    # Exit a parse tree produced by CprestoParser#expr.
    def exitExpr(self, ctx:CprestoParser.ExprContext):
        pass


    # Enter a parse tree produced by CprestoParser#opassign_op.
    def enterOpassign_op(self, ctx:CprestoParser.Opassign_opContext):
        pass

    # Exit a parse tree produced by CprestoParser#opassign_op.
    def exitOpassign_op(self, ctx:CprestoParser.Opassign_opContext):
        pass


    # Enter a parse tree produced by CprestoParser#expr10.
    def enterExpr10(self, ctx:CprestoParser.Expr10Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr10.
    def exitExpr10(self, ctx:CprestoParser.Expr10Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr9.
    def enterExpr9(self, ctx:CprestoParser.Expr9Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr9.
    def exitExpr9(self, ctx:CprestoParser.Expr9Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr8.
    def enterExpr8(self, ctx:CprestoParser.Expr8Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr8.
    def exitExpr8(self, ctx:CprestoParser.Expr8Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr7.
    def enterExpr7(self, ctx:CprestoParser.Expr7Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr7.
    def exitExpr7(self, ctx:CprestoParser.Expr7Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr6.
    def enterExpr6(self, ctx:CprestoParser.Expr6Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr6.
    def exitExpr6(self, ctx:CprestoParser.Expr6Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr5.
    def enterExpr5(self, ctx:CprestoParser.Expr5Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr5.
    def exitExpr5(self, ctx:CprestoParser.Expr5Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr4.
    def enterExpr4(self, ctx:CprestoParser.Expr4Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr4.
    def exitExpr4(self, ctx:CprestoParser.Expr4Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr3.
    def enterExpr3(self, ctx:CprestoParser.Expr3Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr3.
    def exitExpr3(self, ctx:CprestoParser.Expr3Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr2.
    def enterExpr2(self, ctx:CprestoParser.Expr2Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr2.
    def exitExpr2(self, ctx:CprestoParser.Expr2Context):
        pass


    # Enter a parse tree produced by CprestoParser#expr1.
    def enterExpr1(self, ctx:CprestoParser.Expr1Context):
        pass

    # Exit a parse tree produced by CprestoParser#expr1.
    def exitExpr1(self, ctx:CprestoParser.Expr1Context):
        pass


    # Enter a parse tree produced by CprestoParser#term.
    def enterTerm(self, ctx:CprestoParser.TermContext):
        pass

    # Exit a parse tree produced by CprestoParser#term.
    def exitTerm(self, ctx:CprestoParser.TermContext):
        pass


    # Enter a parse tree produced by CprestoParser#unary.
    def enterUnary(self, ctx:CprestoParser.UnaryContext):
        pass

    # Exit a parse tree produced by CprestoParser#unary.
    def exitUnary(self, ctx:CprestoParser.UnaryContext):
        pass


    # Enter a parse tree produced by CprestoParser#postfix.
    def enterPostfix(self, ctx:CprestoParser.PostfixContext):
        pass

    # Exit a parse tree produced by CprestoParser#postfix.
    def exitPostfix(self, ctx:CprestoParser.PostfixContext):
        pass


    # Enter a parse tree produced by CprestoParser#args.
    def enterArgs(self, ctx:CprestoParser.ArgsContext):
        pass

    # Exit a parse tree produced by CprestoParser#args.
    def exitArgs(self, ctx:CprestoParser.ArgsContext):
        pass


    # Enter a parse tree produced by CprestoParser#primary.
    def enterPrimary(self, ctx:CprestoParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CprestoParser#primary.
    def exitPrimary(self, ctx:CprestoParser.PrimaryContext):
        pass


    # Enter a parse tree produced by CprestoParser#compilation_unit.
    def enterCompilation_unit(self, ctx:CprestoParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by CprestoParser#compilation_unit.
    def exitCompilation_unit(self, ctx:CprestoParser.Compilation_unitContext):
        pass


    # Enter a parse tree produced by CprestoParser#declaration_file.
    def enterDeclaration_file(self, ctx:CprestoParser.Declaration_fileContext):
        pass

    # Exit a parse tree produced by CprestoParser#declaration_file.
    def exitDeclaration_file(self, ctx:CprestoParser.Declaration_fileContext):
        pass



del CprestoParser