import ir
from .Node import Node
from .ExprStmtNode import ExprStmtNode
from .ReturnNode import ReturnNode

class AST(Node):
    NUM_LEFT_COLUMNS = 24

    def __init__(self,source,declarations):
        super().__init__()
        self.source = source
        self._declarations = declarations
        self.scope = None
        self.constant_table = None
    
    def location(self):
        return self.source
    
    def types(self):
        result = []
        result += self._declarations.defstructs()
        result += self._declarations.defunions()
        result += self._declarations.typedefs()
        return result

    def entities(self):
        result = []
        result += self._declarations.funcdecls()
        result += self._declarations.vardecls()
        result += self._declarations.defvars()
        result += self._declarations.defuns()
        result += self._declarations.constants()
        return result
    
    def declarations(self):
        result = []
        result += self._declarations.funcdecls()
        result += self._declarations.vardecls()
        return result
    
    def definitions(self):
        result = []
        result += self._declarations.defvars()
        result += self._declarations.defuns()
        result += self._declarations.constants()
        return result
    
    def constants(self):
        return self._declarations.constants()
    
    def defined_variables(self):
        return self._declarations.defvars()
    
    def defined_functions(self):
        return self._declarations.defuns()
    
    #called by LocalResolver
    def set_scope(self,scope):
        if self.scope != None:
            raise Exception("must not happen: ToplevelScope set twice")
        self.scope = scope
    
    def scope(self):
        if self.scope != None:
            raise Exception("must not happen: AST.scope is null")
        return self.scope

    #called by LocalResolver
    def set_constant_table(self,table):
        if self.constant_table != None:
            raise Exception("must not happen: ConstantTable set twice")
        self.constant_table = table
    
    def constant_table(self):
        if self.constant_table == None:
            raise Exception("must not happen: AST.ConstantTable is null")
        return self.constant_table
    
    def ir(self):
        return IR(self.source,
                self._declarations.defvars(),
                self._declarations.defuns(),
                self._declarations.funcdecls(),
                self.scope,
                self.constant_table)
    
    def _dump(self,dumper):
        dumper.print_node_list("variables", self.defined_variables())
        dumper.print_node_list("functions", self.defined_functions())
    
    def dump_tokens(self,s):
        for t in self.source.token():
            self.print_pair(t.kind_name(), t.dumped_image(), s)
    
    def print_pair(self,key,value,s):
        s.write(key)
        for n in range(AST.NUM_LEFT_COLUMNS,0,-1):
            s.write(" ")
        s.write(value+"\n")

    def get_single_main_stmt(self):
        for f in self.defined_functions():
            if f.name() == "main":
                if len(f.body().stmts()) == 0:
                    return None
                return f.body().stmts()[0]
        return None
    
    def get_single_main_expr(self):
        stmt = self.get_single_main_stmt()
        if stmt == None:
            return None
        elif isinstance(stmt, ExprStmtNode):
            return stmt.expr()
        elif isinstance(stmt, ReturnNode):
            return stmt.expr()
        else:
            return None

