grammar Cpresto;

options { language=Python3; }

@header
{
from ..ast.AbstractAssignNode import *
from ..ast.AdressNode import *
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
from ..exception.SyntaxException import *

}

@parser::members 
{

@classmethod
def parse_file(file,loader,error_handler,debug=None):
        if debug == None:
                debug = False
        return self.new_file_parser(file,loader,error_handler,debug).parse()

@classmethod
def parse_decl_file(file,loader,error_handler,debug=None):
        if debug == None:
                debug = False
        return self.new_file_parser(file,loader,error_handler,debug).parse_decls()

@classmethod
def new_file_parser(filename,loader,error_handler,debug):
        try:
                input_stream = FileStream(filename)
                lexer = CprestoLexer(input_stream)
                stream = CommonTokenStream(lexer)
                return CprestoParser.parser_init(stream,filename,loader,error_handler,debug)
        except FileNotFoundError as ex:
                raise FileException(ex.message)
        except Exception as ex:
                raise Exception("UTF-8 is not supported?: "+ex.message)

#__init__ is not overriden
@classmethod
def parser_init(s,name,loader,error_handler,debug=None):
        parser = CprestoParser(s)
        parser.source_name = name
        parser.loader = loader
        parser.error_handler = error_handler
        parser.known_typedefs = set()
        return parser

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
        idx = 0
        buf = ""
        image = _image[1:-1]
        while (idx = image.index("\\",pos)) >= 0:
                buf += image[pos:idx]
                if len(image) >= idx + 4 and image[idx+1].isdigit() and \
                   image[idx+2].isdigit() and image[idx+3].isdigit():
                        buf += self.unescape_octal(image[idx+1:idx+4])
                        pos = idx + 4
                else :
                        buf += self.unescape_seq(image[idx+1])
                        pos = idx + 2
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
        return Location(self.source_name,t)

} // @parser::members



//----parser rules----
import_stmts returns [res] locals [decls,impdecls=Declarations()] :
        (libid=import_stmt
{
try:
        $decls = self.loader.load_library(libid,self.error_handler)
        if $decls != None:
                $impdecls.add($decls)
                self.add_known_typedefs($decls.typedefs())
except CompileException as ex:
        raise ParseException(ex.message)
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



name returns [res] locals [] : 
        t=IDENTIFIER 
{
        $res = $t.text
};

top_defs returns [res] locals [decls=Declarations()] :
        ( df=defun      
{ 
$decls.add_defun(df) 
}
        | dv=defvars    
{ 
$decls.add_defvars(dv) 
}
        | dc=defconst   
{ 
$decls.add_constant(dc) 
}
        | ds=defstruct  
{ 
$decls.add_defstruct(ds) 
}
        | du=defunion  
{ 
$decls.add_defunion(du) 
}
        | td=typedef    
{ 
$decls.add_typedef(td) 
}
        )*
{ 
$res = $decls 
} ;

defvars returns [res] locals [defs=list(),initflag=False] :
        priv=storage t=typename n=name ('=' init=expr 
{
if init != None:
        $initflag = True
}       
        )? 
{
$defs.append(DefinedVariable(priv,t,n,None) if not $initflag else DefinedVariable(priv,t,n,init))
$initflag=False
}
        ( ',' n=name ('=' init=expr 
{
if init != None:
        $initflag = True
}       
        )?
{
$defs.append(DefinedVariable(priv,t,n,None) if not $initflag else DefinedVariable(priv,t,n,init))
$initflag=False
}
        )* ';'
{
$res = $defs
} ;


storage returns [res] locals [] :
        (t=STATIC)?
{
$res = False if t == None else True
} ;

defun returns [res] locals [t] :
        priv=storage ret=typeref n=name '(' ps=params ')' body=block
{
$t = FunctionTypeRef(ret,ps.parameters_type_ref()); 
$res = DefinedFunction(priv,TypeNode($t),n,ps,body)
} ;

params      : VOID | fixedparams (',' '...')? ;
fixedparams : param (',' param)* ;
param       : typename name ;
block returns [res] locals [] :
        t='{' v=defvar_list s=stmts '}'
        {$res = BlockNode(location($t),$v,$s)} ;

defvar_list returns [res] locals [l=list()] :
        (vars=defvars { $l += $vars })*
        {$res = $l} ;

defconst    : CONST typename name '=' expr ';' ;
defstruct   : STRUCT name member_list ';' ;
defunion    : UNION  name member_list ';' ;
member_list : '{' (slot ';')* '}' ;
slot        : typename name ;
typedef     : TYPEDEF typeref IDENTIFIER ';' ;

typename    : typeref ;
typeref     : typeref_base
              ('[' ']'
              | '[' INTEGER ']'
              | '*' 
              | '(' param_typerefs ')')* ;
param_typerefs : VOID 
               | fixedparam_typerefs (',' '...' )? ;
fixedparam_typerefs :  typeref (',' typeref)* ;

typeref_base : VOID  
             | CHAR 
             | SHORT 
             | INT 
             | LONG 
             | UNSIGNED CHAR
             | UNSIGNED SHORT
             | UNSIGNED INT
             | UNSIGNED LONG
             | STRUCT IDENTIFIER
             | UNION IDENTIFIER 
             | IDENTIFIER ; //typeとして登録されてるもののみ許可する必要


stmts returns [res] locals [ss=list()] :
        (s=stmt {if $s != None:{ $ss.append($s) }})*
        {$res = $ss} ; 

stmt         : ';'
             | labeled_stmt 
             | expr ';'
             | block 
             | if_stmt
             | while_stmt
             | dowhile_stmt
             | for_stmt
             | switch_stmt
             | break_stmt
             | continue_stmt
             | goto_stmt
             | return_stmt ;
labeled_stmt : IDENTIFIER ':' stmt ;
if_stmt returns [res] locals [elseflag=False] :
        t=IF '(' cond=expr ')' thenbody=stmt (ELSE elsebody=stmt {$elseflag=True})?
        {$res = IfNode(location($t),$cond,$thenbody,None) if not $elseflag else IfNode(location($t),$cond,$thenbody,$elsebody)} ;

while_stmt returns [res] locals [] :
        t=WHILE '(' cond=expr ')' body=stmt
        {$res = WhileNode(location($t),$cond,$body)} ;
dowhile_stmt : DO stmt WHILE '(' expr ')' ';' ;
for_stmt     : FOR '(' (expr)? ';' (expr)? ';' (expr)? ')' stmt ;
switch_stmt  : SWITCH '(' expr ')' '{' case_clauses '}' ;
case_clauses : (case_clause)* ;
case_clause  : cases case_body ;
cases        : (CASE primary ':')+ ;
default_clause : DEFAULT ':' case_body;
case_body    : (stmt)+ ;
break_stmt   : BREAK ';' ;
continue_stmt: CONTINUE ';' ;
goto_stmt    : GOTO IDENTIFIER ';' ;
return_stmt  : RETURN ';' 
             | RETURN expr ';' ;

expr returns [res] locals [] :
        lhs=term '=' rhs=expr
        {$res = AssignNode($lhs,$rhs)}
        | lhs=term op=opassign_op rhs=expr
          {$res = OpAssignNode($lhs,$op,$rhs)}
        | e=expr10
          {$res = $e} ;

opassign_op returns [res] locals [] :
          '+=' {$res = '+'}
        | '-=' {$res = '-'}
        | '*=' {$res = '*'}
        | '/=' {$res = '/'}
        | '%=' {$res = '%'}
        | '&=' {$res = '&'}
        | '|=' {$res = '|'}
        | '^=' {$res = '^'}
        | '<<=' {$res = '<<'}
        | '>>=' {$res = '>>'} ;

expr10 returns [res] locals [] :
        c=expr9 {$res = $c}
        ('?' t=expr ':' e=expr10
                 {$res = CondExprNode($c,$t,$e)})? ;

expr9 returns [res] locals [] :
        l=expr8
        ('||' r=expr8  {$l = LogicalOrNode($l,$r)}
        )*
        {$res = $l} ;

expr8 returns [res] locals [] :
        l=expr7
        ('&&' r=expr7  {$l = LogicalAndNode($l,$r)}
        )*
        {$res = $l} ;

expr7 returns [res] locals [] :
        l=expr6
        ('>' r=expr6 {$l = BinaryOpNode($l,'>',$r)}
        |'<' r=expr6 {$l = BinaryOpNode($l,'<',$r)}
        |'>=' r=expr6 {$l = BinaryOpNode($l,'>=',$r)}
        |'<=' r=expr6 {$l = BinaryOpNode($l,'<=',$r)}
        |'==' r=expr6 {$l = BinaryOpNode($l,'==',$r)}
        |'!=' r=expr6 {$l = BinaryOpNode($l,'!=',$r)}
        )*
        {$res = $l} ;

expr6 returns [res] locals [] :
        l=expr5 
        ('|' r=expr5  {$l = BinaryOpNode($l,'|',$r)}
        )*
        {$res = $l} ;

expr5 returns [res] locals [] :
        l=expr4 
        ('^' r=expr4  {$l = BinaryOpNode($l,'^',$r)}
        )*
        {$res = $l} ;

expr4 returns [res] locals [] :
        l=expr3 
        ('&' r=expr3  {$l = BinaryOpNode($l,'&',$r)}
        )*
        {$res = $l} ;

expr3 returns [res] locals [] :
        l=expr2 
        ('>>' r=expr2  {$l = BinaryOpNode($l,'>>',$r)}
        |'<<' r=expr2  {$l = BinaryOpNode($l,'<<',$r)}
        )*
        {$res = $l} ;

expr2 returns [res] locals [] :
        l=expr1
        ('+' r=expr1  {$l = BinaryOpNode($l,'+',$r)}
        |'-' r=expr1  {$l = BinaryOpNode($l,'-',$r)}
        )*
        {$res = $l} ;

expr1 returns [res] locals [] :
        l=term 
        ('*' r=term  {$l = BinaryOpNode($l,'*',$r)}
        |'/' r=term  {$l = BinaryOpNode($l,'/',$r)}
        |'%' r=term  {$l = BinaryOpNode($l,'%',$r)}
        )*
        {$res = $l} ;

term returns [res] locals [] :
        '(' t=typename ')' n=term {$res = CastNode($t,$n)} |
        u=unary                   {$res = $u};

unary returns [res] locals [] :
        '++' n=unary   {$res = PrefixOpNode('++',$n)} |
        '--' n=unary   {$res = PrefixOpNode('--',$n)} |
        '+'  m=term    {$res = UnaryOpNode('+',$m)}   |
        '-'  m=term    {$res = UnaryOpNode('-',$m)}   |
        '!'  m=term    {$res = UnaryOpNode('!',$m)}   |
        '~'  m=term    {$res = UnaryOpNode('~',$m)}   |
        '*'  m=term    {$res = DereferenceNode($m)}   |
        '&'  m=term    {$res = AddressNode($m)}       |
        SIZEOF '(' t=typename ')' {$res = SizeofTypeNode($t,size_t())} |
        SIZEOF n=unary {$res = SizeofExprNode($n,size_t())} |
        p=postfix      {$res = $p} ;

postfix returns [res] locals [] :
        e=primary 
        ('++'                   {$e = SuffixOpNode('++',$e)}
        |'--'                   {$e = SuffixOpNode('--',$e)}
        |'[' idx=expr ']'       {$e = ArefNode($e,$idx)}
        |'.' memb=name          {$e = MemberNode($e,$memb)}
        |'->' memb=name         {$e = PtrMemberNode($e,$memb)}
        |'(' ags=args ')'       {$e = FuncallNode($e,$ags)}   
        )*
        {res = $e} ;
        

args         : (expr (',' expr)*)? ;
primary returns [res] locals []:
        t=INTEGER {$res =  integer_node(location($t),$t.text)} |
        t=CHARACTER {$res =  IntegerLiteralNode(location($t),IntegerTypeRef.char_ref(),character_code($t.text))} |
        t=STRING {$res =  StringLiteralNode(location($t),PointerTypeRef(IntegerTypeRef.char_ref()),string_value($t.text))} |
        t=IDENTIFIER {$res =  VariableNode(loc=location($t),name=$t.text)} |
        '(' e=expr ')' {$res = $e};

compilation_unit returns [res] locals [t] :
{
$t = self._input.LT(1)
}
        impdecls=import_stmts decls=top_defs
{
decls.add(impdecls)
$res=AST(self.location($t),decls) 
} ;

declaration_file returns [res] locals [decls=Declarations()] :
        impdecls=import_stmts
{ 
$decls.add(impdecls)
}
        (fdecl=funcdecl
{ 
$decls.add(fdecl)
}   
        |vdecl=vardecl
{
$decls.add(vdecl)
}
        |defc=defconst
{
$decls.add(defc)
}
        |defs=defstruct
{
$decls.add(defs)
}
        |defu=defunion
{
$decls.add(defu)
}
        |tdef=typedef
{
$decls.add(tdef)
}
        )*
{
$res = $decls
} ;




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