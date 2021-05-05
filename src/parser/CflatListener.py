# Generated from Cflat.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CflatParser import CflatParser
else:
    from CflatParser import CflatParser

# This class defines a complete listener for a parse tree produced by CflatParser.
class CflatListener(ParseTreeListener):

    # Enter a parse tree produced by CflatParser#import_stmts.
    def enterImport_stmts(self, ctx:CflatParser.Import_stmtsContext):
        pass

    # Exit a parse tree produced by CflatParser#import_stmts.
    def exitImport_stmts(self, ctx:CflatParser.Import_stmtsContext):
        pass


    # Enter a parse tree produced by CflatParser#import_stmt.
    def enterImport_stmt(self, ctx:CflatParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#import_stmt.
    def exitImport_stmt(self, ctx:CflatParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#name.
    def enterName(self, ctx:CflatParser.NameContext):
        pass

    # Exit a parse tree produced by CflatParser#name.
    def exitName(self, ctx:CflatParser.NameContext):
        pass


    # Enter a parse tree produced by CflatParser#top_defs.
    def enterTop_defs(self, ctx:CflatParser.Top_defsContext):
        pass

    # Exit a parse tree produced by CflatParser#top_defs.
    def exitTop_defs(self, ctx:CflatParser.Top_defsContext):
        pass


    # Enter a parse tree produced by CflatParser#defvars.
    def enterDefvars(self, ctx:CflatParser.DefvarsContext):
        pass

    # Exit a parse tree produced by CflatParser#defvars.
    def exitDefvars(self, ctx:CflatParser.DefvarsContext):
        pass


    # Enter a parse tree produced by CflatParser#storage.
    def enterStorage(self, ctx:CflatParser.StorageContext):
        pass

    # Exit a parse tree produced by CflatParser#storage.
    def exitStorage(self, ctx:CflatParser.StorageContext):
        pass


    # Enter a parse tree produced by CflatParser#defun.
    def enterDefun(self, ctx:CflatParser.DefunContext):
        pass

    # Exit a parse tree produced by CflatParser#defun.
    def exitDefun(self, ctx:CflatParser.DefunContext):
        pass


    # Enter a parse tree produced by CflatParser#params.
    def enterParams(self, ctx:CflatParser.ParamsContext):
        pass

    # Exit a parse tree produced by CflatParser#params.
    def exitParams(self, ctx:CflatParser.ParamsContext):
        pass


    # Enter a parse tree produced by CflatParser#fixedparams.
    def enterFixedparams(self, ctx:CflatParser.FixedparamsContext):
        pass

    # Exit a parse tree produced by CflatParser#fixedparams.
    def exitFixedparams(self, ctx:CflatParser.FixedparamsContext):
        pass


    # Enter a parse tree produced by CflatParser#param.
    def enterParam(self, ctx:CflatParser.ParamContext):
        pass

    # Exit a parse tree produced by CflatParser#param.
    def exitParam(self, ctx:CflatParser.ParamContext):
        pass


    # Enter a parse tree produced by CflatParser#block.
    def enterBlock(self, ctx:CflatParser.BlockContext):
        pass

    # Exit a parse tree produced by CflatParser#block.
    def exitBlock(self, ctx:CflatParser.BlockContext):
        pass


    # Enter a parse tree produced by CflatParser#defvar_list.
    def enterDefvar_list(self, ctx:CflatParser.Defvar_listContext):
        pass

    # Exit a parse tree produced by CflatParser#defvar_list.
    def exitDefvar_list(self, ctx:CflatParser.Defvar_listContext):
        pass


    # Enter a parse tree produced by CflatParser#defconst.
    def enterDefconst(self, ctx:CflatParser.DefconstContext):
        pass

    # Exit a parse tree produced by CflatParser#defconst.
    def exitDefconst(self, ctx:CflatParser.DefconstContext):
        pass


    # Enter a parse tree produced by CflatParser#defstruct.
    def enterDefstruct(self, ctx:CflatParser.DefstructContext):
        pass

    # Exit a parse tree produced by CflatParser#defstruct.
    def exitDefstruct(self, ctx:CflatParser.DefstructContext):
        pass


    # Enter a parse tree produced by CflatParser#defunion.
    def enterDefunion(self, ctx:CflatParser.DefunionContext):
        pass

    # Exit a parse tree produced by CflatParser#defunion.
    def exitDefunion(self, ctx:CflatParser.DefunionContext):
        pass


    # Enter a parse tree produced by CflatParser#member_list.
    def enterMember_list(self, ctx:CflatParser.Member_listContext):
        pass

    # Exit a parse tree produced by CflatParser#member_list.
    def exitMember_list(self, ctx:CflatParser.Member_listContext):
        pass


    # Enter a parse tree produced by CflatParser#slot.
    def enterSlot(self, ctx:CflatParser.SlotContext):
        pass

    # Exit a parse tree produced by CflatParser#slot.
    def exitSlot(self, ctx:CflatParser.SlotContext):
        pass


    # Enter a parse tree produced by CflatParser#typedef.
    def enterTypedef(self, ctx:CflatParser.TypedefContext):
        pass

    # Exit a parse tree produced by CflatParser#typedef.
    def exitTypedef(self, ctx:CflatParser.TypedefContext):
        pass


    # Enter a parse tree produced by CflatParser#typename.
    def enterTypename(self, ctx:CflatParser.TypenameContext):
        pass

    # Exit a parse tree produced by CflatParser#typename.
    def exitTypename(self, ctx:CflatParser.TypenameContext):
        pass


    # Enter a parse tree produced by CflatParser#typeref.
    def enterTyperef(self, ctx:CflatParser.TyperefContext):
        pass

    # Exit a parse tree produced by CflatParser#typeref.
    def exitTyperef(self, ctx:CflatParser.TyperefContext):
        pass


    # Enter a parse tree produced by CflatParser#param_typerefs.
    def enterParam_typerefs(self, ctx:CflatParser.Param_typerefsContext):
        pass

    # Exit a parse tree produced by CflatParser#param_typerefs.
    def exitParam_typerefs(self, ctx:CflatParser.Param_typerefsContext):
        pass


    # Enter a parse tree produced by CflatParser#fixedparam_typerefs.
    def enterFixedparam_typerefs(self, ctx:CflatParser.Fixedparam_typerefsContext):
        pass

    # Exit a parse tree produced by CflatParser#fixedparam_typerefs.
    def exitFixedparam_typerefs(self, ctx:CflatParser.Fixedparam_typerefsContext):
        pass


    # Enter a parse tree produced by CflatParser#typeref_base.
    def enterTyperef_base(self, ctx:CflatParser.Typeref_baseContext):
        pass

    # Exit a parse tree produced by CflatParser#typeref_base.
    def exitTyperef_base(self, ctx:CflatParser.Typeref_baseContext):
        pass


    # Enter a parse tree produced by CflatParser#stmts.
    def enterStmts(self, ctx:CflatParser.StmtsContext):
        pass

    # Exit a parse tree produced by CflatParser#stmts.
    def exitStmts(self, ctx:CflatParser.StmtsContext):
        pass


    # Enter a parse tree produced by CflatParser#stmt.
    def enterStmt(self, ctx:CflatParser.StmtContext):
        pass

    # Exit a parse tree produced by CflatParser#stmt.
    def exitStmt(self, ctx:CflatParser.StmtContext):
        pass


    # Enter a parse tree produced by CflatParser#labeled_stmt.
    def enterLabeled_stmt(self, ctx:CflatParser.Labeled_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#labeled_stmt.
    def exitLabeled_stmt(self, ctx:CflatParser.Labeled_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#if_stmt.
    def enterIf_stmt(self, ctx:CflatParser.If_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#if_stmt.
    def exitIf_stmt(self, ctx:CflatParser.If_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#while_stmt.
    def enterWhile_stmt(self, ctx:CflatParser.While_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#while_stmt.
    def exitWhile_stmt(self, ctx:CflatParser.While_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#dowhile_stmt.
    def enterDowhile_stmt(self, ctx:CflatParser.Dowhile_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#dowhile_stmt.
    def exitDowhile_stmt(self, ctx:CflatParser.Dowhile_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#for_stmt.
    def enterFor_stmt(self, ctx:CflatParser.For_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#for_stmt.
    def exitFor_stmt(self, ctx:CflatParser.For_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#switch_stmt.
    def enterSwitch_stmt(self, ctx:CflatParser.Switch_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#switch_stmt.
    def exitSwitch_stmt(self, ctx:CflatParser.Switch_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#case_clauses.
    def enterCase_clauses(self, ctx:CflatParser.Case_clausesContext):
        pass

    # Exit a parse tree produced by CflatParser#case_clauses.
    def exitCase_clauses(self, ctx:CflatParser.Case_clausesContext):
        pass


    # Enter a parse tree produced by CflatParser#case_clause.
    def enterCase_clause(self, ctx:CflatParser.Case_clauseContext):
        pass

    # Exit a parse tree produced by CflatParser#case_clause.
    def exitCase_clause(self, ctx:CflatParser.Case_clauseContext):
        pass


    # Enter a parse tree produced by CflatParser#cases.
    def enterCases(self, ctx:CflatParser.CasesContext):
        pass

    # Exit a parse tree produced by CflatParser#cases.
    def exitCases(self, ctx:CflatParser.CasesContext):
        pass


    # Enter a parse tree produced by CflatParser#default_clause.
    def enterDefault_clause(self, ctx:CflatParser.Default_clauseContext):
        pass

    # Exit a parse tree produced by CflatParser#default_clause.
    def exitDefault_clause(self, ctx:CflatParser.Default_clauseContext):
        pass


    # Enter a parse tree produced by CflatParser#case_body.
    def enterCase_body(self, ctx:CflatParser.Case_bodyContext):
        pass

    # Exit a parse tree produced by CflatParser#case_body.
    def exitCase_body(self, ctx:CflatParser.Case_bodyContext):
        pass


    # Enter a parse tree produced by CflatParser#break_stmt.
    def enterBreak_stmt(self, ctx:CflatParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#break_stmt.
    def exitBreak_stmt(self, ctx:CflatParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#continue_stmt.
    def enterContinue_stmt(self, ctx:CflatParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#continue_stmt.
    def exitContinue_stmt(self, ctx:CflatParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#goto_stmt.
    def enterGoto_stmt(self, ctx:CflatParser.Goto_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#goto_stmt.
    def exitGoto_stmt(self, ctx:CflatParser.Goto_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#return_stmt.
    def enterReturn_stmt(self, ctx:CflatParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by CflatParser#return_stmt.
    def exitReturn_stmt(self, ctx:CflatParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by CflatParser#expr.
    def enterExpr(self, ctx:CflatParser.ExprContext):
        pass

    # Exit a parse tree produced by CflatParser#expr.
    def exitExpr(self, ctx:CflatParser.ExprContext):
        pass


    # Enter a parse tree produced by CflatParser#opassign_op.
    def enterOpassign_op(self, ctx:CflatParser.Opassign_opContext):
        pass

    # Exit a parse tree produced by CflatParser#opassign_op.
    def exitOpassign_op(self, ctx:CflatParser.Opassign_opContext):
        pass


    # Enter a parse tree produced by CflatParser#expr10.
    def enterExpr10(self, ctx:CflatParser.Expr10Context):
        pass

    # Exit a parse tree produced by CflatParser#expr10.
    def exitExpr10(self, ctx:CflatParser.Expr10Context):
        pass


    # Enter a parse tree produced by CflatParser#expr9.
    def enterExpr9(self, ctx:CflatParser.Expr9Context):
        pass

    # Exit a parse tree produced by CflatParser#expr9.
    def exitExpr9(self, ctx:CflatParser.Expr9Context):
        pass


    # Enter a parse tree produced by CflatParser#expr8.
    def enterExpr8(self, ctx:CflatParser.Expr8Context):
        pass

    # Exit a parse tree produced by CflatParser#expr8.
    def exitExpr8(self, ctx:CflatParser.Expr8Context):
        pass


    # Enter a parse tree produced by CflatParser#expr7.
    def enterExpr7(self, ctx:CflatParser.Expr7Context):
        pass

    # Exit a parse tree produced by CflatParser#expr7.
    def exitExpr7(self, ctx:CflatParser.Expr7Context):
        pass


    # Enter a parse tree produced by CflatParser#expr6.
    def enterExpr6(self, ctx:CflatParser.Expr6Context):
        pass

    # Exit a parse tree produced by CflatParser#expr6.
    def exitExpr6(self, ctx:CflatParser.Expr6Context):
        pass


    # Enter a parse tree produced by CflatParser#expr5.
    def enterExpr5(self, ctx:CflatParser.Expr5Context):
        pass

    # Exit a parse tree produced by CflatParser#expr5.
    def exitExpr5(self, ctx:CflatParser.Expr5Context):
        pass


    # Enter a parse tree produced by CflatParser#expr4.
    def enterExpr4(self, ctx:CflatParser.Expr4Context):
        pass

    # Exit a parse tree produced by CflatParser#expr4.
    def exitExpr4(self, ctx:CflatParser.Expr4Context):
        pass


    # Enter a parse tree produced by CflatParser#expr3.
    def enterExpr3(self, ctx:CflatParser.Expr3Context):
        pass

    # Exit a parse tree produced by CflatParser#expr3.
    def exitExpr3(self, ctx:CflatParser.Expr3Context):
        pass


    # Enter a parse tree produced by CflatParser#expr2.
    def enterExpr2(self, ctx:CflatParser.Expr2Context):
        pass

    # Exit a parse tree produced by CflatParser#expr2.
    def exitExpr2(self, ctx:CflatParser.Expr2Context):
        pass


    # Enter a parse tree produced by CflatParser#expr1.
    def enterExpr1(self, ctx:CflatParser.Expr1Context):
        pass

    # Exit a parse tree produced by CflatParser#expr1.
    def exitExpr1(self, ctx:CflatParser.Expr1Context):
        pass


    # Enter a parse tree produced by CflatParser#term.
    def enterTerm(self, ctx:CflatParser.TermContext):
        pass

    # Exit a parse tree produced by CflatParser#term.
    def exitTerm(self, ctx:CflatParser.TermContext):
        pass


    # Enter a parse tree produced by CflatParser#unary.
    def enterUnary(self, ctx:CflatParser.UnaryContext):
        pass

    # Exit a parse tree produced by CflatParser#unary.
    def exitUnary(self, ctx:CflatParser.UnaryContext):
        pass


    # Enter a parse tree produced by CflatParser#postfix.
    def enterPostfix(self, ctx:CflatParser.PostfixContext):
        pass

    # Exit a parse tree produced by CflatParser#postfix.
    def exitPostfix(self, ctx:CflatParser.PostfixContext):
        pass


    # Enter a parse tree produced by CflatParser#args.
    def enterArgs(self, ctx:CflatParser.ArgsContext):
        pass

    # Exit a parse tree produced by CflatParser#args.
    def exitArgs(self, ctx:CflatParser.ArgsContext):
        pass


    # Enter a parse tree produced by CflatParser#primary.
    def enterPrimary(self, ctx:CflatParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CflatParser#primary.
    def exitPrimary(self, ctx:CflatParser.PrimaryContext):
        pass


    # Enter a parse tree produced by CflatParser#compilation_unit.
    def enterCompilation_unit(self, ctx:CflatParser.Compilation_unitContext):
        pass

    # Exit a parse tree produced by CflatParser#compilation_unit.
    def exitCompilation_unit(self, ctx:CflatParser.Compilation_unitContext):
        pass



del CflatParser