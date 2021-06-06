grammar Cpresto;

options { language=Python3; }

@parser::header
{
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

}

@parser::members 
{
def parse(self):
        try:
                return self.compilation_unit()
        except Exception as ex:
                raise SyntaxException(str(ex))

def parse_decls(self):
        try:
                return self.declaration_file()
        except Exception as ex:
                raise SyntaxException(str(ex))

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
        idx = image.find("\\",pos)
        while idx >= 0:
                buf += image[pos:idx]
                if len(image) >= idx + 4 and image[idx+1].isdigit() and \
                   image[idx+2].isdigit() and image[idx+3].isdigit():
                        buf += self.unescape_octal(image[idx+1:idx+4])
                        pos = idx + 4
                else :
                        buf += self.unescape_seq(image[idx+1])
                        pos = idx + 2
                idx = image.find("\\",pos)
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

} // @parser::members



//----parser rules----
import_stmts returns [res] locals [decls,impdecls=Declarations()] :
        (libid=import_stmt
{
try:
        $decls = self.loader.load_library(localctx.libid.res,self.error_handler)
        if $decls != None:
                $impdecls.add($decls)
                self.add_known_typedefs($decls.typedefs())
except CompileException as ex:
        raise RecognitionException(message=ex.message)
}
        )*
{
$res = $impdecls
} ;


import_stmt returns [res] locals [buf=""] :
        IMPORT n=name
{
$buf += $n.text
}
        ('.' n=name
{
$buf += '.' + $n.text
}
        )* ';'
{
$res = $buf
} ;

funcdecl returns [res] locals [t] :
        EXTERN ret=typeref n=name '(' ps=params ')' ';'
{
$t = FunctionTypeRef(localctx.ret.res,localctx.ps.res.parameters_type_ref())
$res = UndefinedFunction(TypeNode($t),localctx.n.res,localctx.ps.res)
} ; // funcdecl


vardecl returns [res] locals [] :
        EXTERN t=typename n=name ';'
{
$res = UndefinedVariable(localctx.t.res,localctx.n.res)
} ; // vardecl


name returns [res] locals [] : 
        t=IDENTIFIER 
{
$res = $t.text
}; // name

top_defs returns [res] locals [decls=Declarations()] :
        ( df=defun      
{ 
$decls.add_defun(localctx.df.res) 
}
        | dv=defvars    
{ 
$decls.add_defvars(localctx.dv.res) 
}
        | dc=defconst   
{ 
$decls.add_constant(localctx.dc.res) 
}
        | ds=defstruct  
{ 
$decls.add_defstruct(localctx.ds.res) 
}
        | du=defunion  
{ 
$decls.add_defunion(localctx.du.res) 
}
        | td=typedef    
{ 
$decls.add_typedef(localctx.td.res) 
}
        )*
{ 
$res = $decls 
} ; // top_defs


defvars returns [res] locals [defs=list(),initflag=False] :
        priv=storage t=typename n=name ('=' init=expr 
{
if localctx.init.res != None:
        $initflag = True
}       
        )? 
{
$defs.append(DefinedVariable(localctx.priv.res,localctx.t.res,localctx.n.res,None) if not $initflag else DefinedVariable(localctx.priv.res,localctx.t.res,localctx.n.res,localctx.init.res))
$initflag=False
}
        ( ',' n=name ('=' init=expr 
{
if init != None:
        $initflag = True
}       
        )?
{
$defs.append(DefinedVariable(localctx.priv.res,localctx.t.res,localctx.n.res,None) if not $initflag else DefinedVariable(localctx.priv.res,localctx.t.res,localctx.n.res,localctx.init.res))
$initflag=False
}
        )* ';'
{
$res = $defs
} ; //defvars


storage returns [res] locals [] :
        (t=STATIC)?
{
$res = False if localctx.t == None else True
} ; // storage

defun returns [res] locals [t] :
        priv=storage ret=typeref n=name '(' ps=params ')' body=block
{
$t = FunctionTypeRef(localctx.ret.res,localctx.ps.res.parameters_type_ref()); 
$res = DefinedFunction(localctx.priv.res,TypeNode($t),localctx.n.res,localctx.ps.res,localctx.body.res)
} ; // defun


params returns [res] locals [] : 
        t=VOID
{
$res = Params(self.location(localctx.t),[])
}
        | pms=fixedparams (',' '...' 
{
localctx.pms.res.accept_varargs()
}
        )?
{
$res = localctx.pms.res
}
 ; // params


fixedparams returns [res] locals [pms=list()] : 
        pm1=param 
{
$pms.append(localctx.pm1.res)
}
        (',' pm=param 
{
if localctx.pm != None:
        $pms.append(localctx.pm.res)
}
        )* 
{
$res = Params(localctx.pm1.res.location(),$pms)
} ; // fixedparams


param returns [res] locals [] : 
        t=typename n=name 
{
$res = Parameter(localctx.t.res,localctx.n.res)
} ; // param


block returns [res] locals [] :
        t='{' v=defvar_list s=stmts '}'
{
$res = BlockNode(self.location(localctx.t),localctx.v.res,localctx.s.res)
} ; // block


defvar_list returns [res] locals [l=list()] :
        (vs=defvars 
{ 
if localctx.vs!= None:
        $l += localctx.vs.res
}
        )*
{
$res = $l
} ; // defvar_list


defconst returns [res] locals [] : 
        CONST t=typename n=name '=' v=expr ';' 
{
$res = Constant(localctx.t.res,localctx.n.res,localctx.v.res)
} ; // defconst


defstruct returns [res] locals [] : 
        t=STRUCT n=name membs=member_list ';' 
{
$res = StructNode(self.location(localctx.t),StructTypeRef(localctx.n.res),localctx.n.res,localctx.membs.res)
} ; // defstruct


defunion returns [res] locals [] : 
        t=UNION n=name membs=member_list ';' 
{
$res = UnionNode(self.location(t),UnionTypeRef(n),n,membs)
} ; // defunion


member_list returns [res] locals [membs=list()] : 
        '{' (s=slot ';'
{
if s != None:
        $membs.append(s)
}
        )* '}' 
{
$res = $membs
} ; // member_list


slot returns [res] locals [] : 
        t=typename n=name 
{
$res = Slot(t,n)
} ; // slot


typedef returns [res] locals [] : 
        t=TYPEDEF ref=typeref newname=IDENTIFIER ';' 
{
self.add_type($newname.text)
$res = TypedefNode(self.location(t),ref,$newname.text)
} ; // typedef



typename returns [res] locals [] : 
        ref=typeref 
{
$res = TypeNode(localctx.ref.res)
} ; // typename


typeref returns [res] locals [] : 
        ref=typeref_base
        ('[' ']'
{
localctx.ref.res = ArrayTypeRef(localctx.ref.res)
}
        | '[' t=INTEGER ']'
{
localctx.ref.res = ArrayTypeRef(localctx.ref.res,self.integer_value($t.text))
}
        | '*' 
{
localctx.ref.res = PointerTypeRef(localctx.ref.res)
}
        | '(' pms=param_typerefs ')'
{
localctx.ref.res = FunctionTypeRef(localctx.ref.res,localctx.pms.res)
}
        )* 
{
$res = localctx.ref.res
} ; // typeref


param_typerefs returns [res] locals [] : 
        VOID 
{
$res = ParamTypeRefs([])
}
        | (pms=fixedparam_typerefs (',' '...' 
{
localctx.pms.res.accept_varargs()
}
        )? 
{
$res = localctx.pms.res
} ) ; // param_typerefs


fixedparam_typerefs returns [res] locals [tmp=list()] :  
        ref=typeref 
{
$tmp.append(localctx.ref.res)
}
        (',' ref=typeref 
{
if localctx.ref != None:
        $tmp.append(localctx.ref.res)
}
        )* 
{
$res = ParamTypeRefs($tmp)
} ; // fixedparam_typerefs


typeref_base returns [res] locals [] : 
        (t=VOID  
{
$res = VoidTypeRef(self.location(localctx.t))
}
        | t=CHAR 
{
$res = IntegerTypeRef.char_ref(self.location(localctx.t))
}
        | t=SHORT 
{
$res = IntegerTypeRef.short_ref(self.location(localctx.t))
}
        | t=INT 
{
$res = IntegerTypeRef.int_ref(self.location(localctx.t))
}
        | t=LONG 
{
$res = IntegerTypeRef.long_ref(self.location(localctx.t))
}
        | t=UNSIGNED CHAR
{
$res = IntegerTypeRef.uchar_ref(self.location(localctx.t))
}
        | t=UNSIGNED SHORT
{
$res = IntegerTypeRef.ushort_ref(self.location(localctx.t))
}
        | t=UNSIGNED INT
{
$res = IntegerTypeRef.uint_ref(self.location(localctx.t))
}
        | t=UNSIGNED LONG
{
$res = IntegerTypeRef.ulong_ref(self.location(localctx.t))
}
        | t=STRUCT i=IDENTIFIER
{
$res = StructTypeRef($i.text,self.location(localctx.t))
}
        | t=UNION i=IDENTIFIER 
{
$res = UnionTypeRef($i.text,self.location(localctx.t))
}
        | {self.is_type(self._input.LT(1).text)}? i=IDENTIFIER 
{
$res = UserTypeRef($i.text,self.location(localctx.t))
} ) ; // typeref_base


stmts returns [res] locals [ss=list()] :
        (s=stmt 
{
if localctx.s != None: 
        $ss.append(localctx.s.res) 
}       
        )*
{
$res = $ss
} ; // stmts


stmt returns [res] locals [] : 
        (';'
{
$res = None
}
        | n=labeled_stmt 
{
$res = localctx.n.res
}
        | e=expr ';'
{
$res = ExprStmtNode(localctx.e.res.location(),localctx.e.res)
}
        | n1=block 
{
$res = localctx.n1.res
}
        | n2=if_stmt
{
$res = localctx.n2.res
}
        | n3=while_stmt
{
$res = localctx.n3.res
}
        | n4=dowhile_stmt
{
$res = localctx.n4.res
}
        | n5=for_stmt
{
$res = localctx.n5.res
}
        | n6=switch_stmt
{
$res = localctx.n6.res
}
        | n7=break_stmt
{
$res = localctx.n7.res
}
        | n8=continue_stmt
{
$res = localctx.n8.res
}
        | n9=goto_stmt
{
$res = localctx.n9.res
}
        | n10=return_stmt
{
$res = localctx.n10.res
}) ; // stmt


labeled_stmt returns [res] locals [] : 
        t=IDENTIFIER ':' n=stmt 
{
$res = LabelNode(self.location(localctx.t), $t.text, localctx.n.res)
} ; // labeled_stmt


if_stmt returns [res] locals []:
        t=IF '(' cond=expr ')' thenbody=stmt (ELSE elsebody=stmt)?
{
$res = IfNode(self.location(localctx.t),localctx.cond.res,localctx.thenbody.res,localctx.elsebody.res)
} ; // if_stmt
        

while_stmt returns [res] locals [] :
        t=WHILE '(' cond=expr ')' body=stmt
{
$res = WhileNode(self.location(localctx.t),localctx.cond.res,localctx.body.res)
} ; // while_stmt


dowhile_stmt returns [res] locals [] : 
        t=DO body=stmt WHILE '(' cond=expr ')' ';' 
{
$res = DoWhileNode(self.location(localctx.t),localctx.body.res,localctx.cond.res)
} ; // dowhle_stmt


for_stmt returns [res] locals [] : 
        t=FOR '(' (ini=expr)? ';' (co=expr)? ';' (incr=expr)? ')' body=stmt 
{
$res = ForNode(self.location(localctx.t),localctx.ini.res,localctx.co.res,localctx.incr.res,localctx.body.res)
} ; // for_stmt


switch_stmt returns [res] locals [] : 
        t=SWITCH '(' cond=expr ')' '{' bodies=case_clauses '}' 
{
$res = SwitchNode(self.location(localctx.t),localctx.cond.res,localctx.bodies.res)
} ; // switch_stmt


case_clauses returns [res] locals [cls=list()] :
        (n=case_clause
{
$cls.append(localctx.n.res)
}
        )* (d=default_clause
{
if localctx.d != None:
        $cls.append(localctx.d.res)
}
        ) ? 
{
$res = $cls
} ; // case_clauses


case_clause returns [res] locals [] :
        values=cases body=case_body 
{
$res = CaseNode(localctx.body.res.location(),localctx.values.res,localctx.body.res)
}; // case_clause


cases returns [res] locals [values=list()] :
        (CASE n=primary ':'
{
$values.append(localctx.n.res)
}
        )+ 
{
$res = $values
} ; // cases

default_clause returns [res] locals [] : 
        DEFAULT ':' body=case_body
{
$res = CaseNode(localctx.body.res.location(),[],localctx.body.res)
} ; // default_clause

case_body returns [res] locals [sts=list()] : 
        (s=stmt 
{
if localctx.s != None:
        $sts.append(localctx.s.res)
}
        )+ 
{
if not isinstance($sts[-1],BreakNode):
        raise ParseException('missing break statement at the last of case clause')
$res = BlockNode($sts[0].location(),[],$sts)
} ; // case_body

break_stmt returns [res] locals [] :
        t=BREAK ';' 
{
$res = BreakNode(self.location(localctx.t))
} ; // break_stmt


continue_stmt returns [res] locals [] :
        t=CONTINUE ';'
{
$res = ContinueNode(self.location(localctx.t))
} ; // continue_stmt


goto_stmt returns [res] locals [] :
        t=GOTO n=IDENTIFIER ';'
{
$res = GotoNode(self.location(localctx.t),$n.text)
} ; // goto_stmt


return_stmt returns [res] locals [] :
        t=RETURN ';'
{
$res = ReturnNode(self.location(localctx.t),None)
}
        | t=RETURN exp=expr ';'
{
$res = ReturnNode(self.location(localctx.t),localctx.exp.res)
} ; // return_stmt


expr returns [res] locals [] :
        lhs=term '=' rhs=expr
{
$res = AssignNode(localctx.lhs.res,localctx.rhs.res)
}
        | lhs=term op=opassign_op rhs=expr
{
$res = OpAssignNode(localctx.lhs.res,localctx.op.res,localctx.rhs.res)
}
        | e=expr10
{
$res = localctx.e.res
} ; // expr


opassign_op returns [res] locals [] :
          '+=' 
{
$res = '+'
}
        | '-=' 
{
$res = '-'
}
        | '*=' 
{
$res = '*'
}
        | '/=' 
{
$res = '/'
}
        | '%=' 
{
$res = '%'
}
        | '&=' 
{
$res = '&'
}
        | '|=' 
{
$res = '|'
}
        | '^=' 
{
$res = '^'
}
        | '<<=' 
{
$res = '<<'
}
        | '>>=' 
{
$res = '>>'
} ; // opassign_op


expr10 returns [res] locals [] :
        c=expr9 
{
$res = localctx.c.res
}
        ('?' t=expr ':' e=expr10
{
if localctx.t != None and localctx.e != None:
        $res = CondExprNode(localctx.c.res,localctx.t.res,localctx.e.res)
}
        )? ; // expr10

expr9 returns [res] locals [] :
        l=expr8 ('||' r=expr8  
{
localctx.l.res = LogicalOrNode(localctx.l.res,localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr9

expr8 returns [res] locals [] :
        l=expr7 ('&&' r=expr7  
{
localctx.l.res = LogicalAndNode(localctx.l.res,localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr8

expr7 returns [res] locals [] :
        l=expr6 ('>' r=expr6 
{
localctx.l.res = BinaryOpNode(localctx.l.res,'>',localctx.r.res)
}
        |'<' r=expr6 
{
localctx.l.res = BinaryOpNode(localctx.l.res,'<',localctx.r.res)
}
        |'>=' r=expr6 
{
localctx.l.res = BinaryOpNode(localctx.l.res,'>=',localctx.r.res)
}
        |'<=' r=expr6 
{
localctx.l.res = BinaryOpNode(localctx.l.res,'<=',localctx.r.res)
}
        |'==' r=expr6 
{
localctx.l.res = BinaryOpNode(localctx.l.res,'==',localctx.r.res)
}
        |'!=' r=expr6 
{
localctx.l.res = BinaryOpNode(localctx.l.res,'!=',localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr7

expr6 returns [res] locals [] :
        l=expr5 ('|' r=expr5  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'|',localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr6

expr5 returns [res] locals [] :
        l=expr4 ('^' r=expr4  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'^',localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr5

expr4 returns [res] locals [] :
        l=expr3 ('&' r=expr3  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'&',localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr4

expr3 returns [res] locals [] :
        l=expr2 ('>>' r=expr2  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'>>',localctx.r.res)
}
        |'<<' r=expr2  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'<<',localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr3

expr2 returns [res] locals [] :
        l=expr1
        ('+' r=expr1  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'+',localctx.r.res)
}
        |'-' r=expr1  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'-',localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr2

expr1 returns [res] locals [] :
        l=term 
        ('*' r=term  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'*',localctx.r.res)
}
        |'/' r=term  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'/',localctx.r.res)
}
        |'%' r=term  
{
localctx.l.res = BinaryOpNode(localctx.l.res,'%',localctx.r.res)
}
        )*
{
$res = localctx.l.res
} ; // expr1

term returns [res] locals [] :
        '(' t=typename ')' n=term 
{
$res = CastNode(localctx.t.res,localctx.n.res)
} 
        | u=unary                   
{
$res = localctx.u.res
} ; // term

unary returns [res] locals [] :
        '++' n=unary   
{
$res = PrefixOpNode('++',localctx.n.res)
}
        |'--' n=unary   
{
$res = PrefixOpNode('--',localctx.n.res)
}
        |'+'  m=term    
{
$res = UnaryOpNode('+',localctx.m.res)
}
        |'-'  m=term    
{
$res = UnaryOpNode('-',localctx.m.res)
}
        |'!'  m=term    
{
$res = UnaryOpNode('!',localctx.m.res)
}
        |'~'  m=term    
{
$res = UnaryOpNode('~',localctx.m.res)
}
        |'*'  m=term    
{
$res = DereferenceNode(localctx.m.res)
}
        |'&'  m=term    
{
$res = AddressNode(localctx.m.res)
}
        |SIZEOF '(' t=typename ')' 
{
$res = SizeofTypeNode(localctx.t.res,self.size_t())
} 
        |SIZEOF n=unary 
{
$res = SizeofExprNode(localctx.n.res,self.size_t())
} 
        |p=postfix      
{
$res = localctx.p.res
} ; // unary

postfix returns [res] locals [tmp] :
        e=primary 
{
$tmp = localctx.e.res
}
        ('++'                   
{
$tmp = SuffixOpNode('++',$tmp)
}
        |'--'                   
{
$tmp = SuffixOpNode('--',$tmp)
}
        |'[' idx=expr ']'       
{
$tmp = ArefNode($tmp,localctx.idx.res)
}
        |'.' memb=name          
{
$tmp = MemberNode($tmp,localctx.memb.res)
}
        |'->' memb=name         
{
$tmp = PtrMemberNode($tmp,localctx.memb.res)
}
        |'(' ags=args ')'       
{
$tmp = FuncallNode($tmp,localctx.ags.res)
}   
        )*
{
$res = $tmp
} ; // postfix
        

args returns [res] locals[ags=list()] : 
        (arg=expr 
{
$ags.append(localctx.arg.res)
}
        (',' arg=expr
{
$ags.append(localctx.arg.res)
}
        )*)? 
{
$res = $ags
} ; // args

primary returns [res] locals []:
        t=INTEGER 
{
$res =  self.integer_node(self.location(localctx.t),$t.text)
} 
        |t=CHARACTER 
{
$res =  IntegerLiteralNode(self.location(localctx.t),IntegerTypeRef.char_ref(),self.character_code($t.text))
} 
        |t=STRING 
{
$res =  StringLiteralNode(self.location(localctx.t),PointerTypeRef(IntegerTypeRef.char_ref()),self.string_value($t.text))
} 
        |t=IDENTIFIER
{
$res =  VariableNode(loc=self.location(localctx.t),name=$t.text)
} 
        |'(' e=expr ')' 
{
$res = localctx.e.res
} ; // primary

compilation_unit returns [res] locals [t] :
{
print(self._input.LT(1).text)
$t = self._input.LT(1)
}
        impdecls=import_stmts decls=top_defs
{
if localctx.impdecls.res != None:
        localctx.decls.res.add(localctx.impdecls.res)
$res=AST(self.location($t),localctx.decls.res) 
} ; // compilation_unit

declaration_file returns [res] locals [decls=Declarations()] :
        impdecls=import_stmts
{ 
$decls.add(localctx.impdecls.res)
}
        (fdecl=funcdecl
{ 
$decls.add(localctx.fdecl.res)
}   
        |vdecl=vardecl
{
$decls.add(localctx.vdecl.res)
}
        |defc=defconst
{
$decls.add(localctx.defc.res)
}
        |defs=defstruct
{
$decls.add(localctx.defs.res)
}
        |defu=defunion
{
$decls.add(localctx.defu.res)
}
        |tdef=typedef
{
$decls.add(localctx.tdef.res)
}
        )*
{
$res = $decls
} ; // declaration_file




//----lexer rules----
VOID     : 'void';
CHAR     : 'char';
SHORT    : 'short';
INT      : 'int';
LONG     : 'long';
STRUCT   : 'struct';
UNION    : 'union';
ENUM     : 'enum';
STATIC   : 'static';
EXTERN   : 'extern';
CONST    : 'const';
SIGNED   : 'signed';
UNSIGNED : 'unsigned';
IF       : 'if';
ELSE     : 'else';
SWITCH   : 'switch';
CASE     : 'case';
DEFAULT  : 'default';
WHILE    : 'while';
DO       : 'do';
FOR      : 'for';
RETURN   : 'return';
BREAK    : 'break';
CONTINUE : 'continue';
GOTO     : 'goto';
TYPEDEF  : 'typedef';
IMPORT   : 'import';
SIZEOF   : 'sizeof';

IDENTIFIER : [a-zA-Z_]([a-zA-Z0-9_])*;

INTEGER : [1-9] ([0-9])* ('U')? ('L')?
        | '0' ('x' | 'X') ([0-9a-fA-F])+ ('U')? ('L')?
        | '0' ([0-7])* ('U')? ('L')?;

SPACES : [ \t\r\n\f]+ -> skip ;

LINE_COMMENT : '//' (~[\n\r])* ('\n' | '\r\n' | '\r')?;

BLOCK_COMMENT : '/*' .*? '*/';

STRING : '"' ('\\"' | . )*? '"';

CHARACTER : '\'' ('\\' . | ~('\\')) '\'';