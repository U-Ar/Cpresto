from type.TypeRef import *
from type.Type import *
from utils.TextUtils import *
from .TypeNode import *
from .Dumpable import *

class Dumper:
    indent_string = "  "

    def __init__(self,s):
        self.stream = s
        self.n_indent = 0
    
    def print_class(self,obj,loc):
        self.print_indent()
        self.stream.write("<<" + obj.get_class().get_simple_name() + ">> ("+loc+")\n")
    
    def print_node_list(self,name,nodes):
        self.print_indent()
        self.stream.write(name+":\n")
        self.indent()
        for n in nodes:
            n.dump(self)
        self.unindent()
    
    def print_member(self,name,value,is_resolved=None):
        if is_resolved != None:
            self.print_pair(name, TextUtils.dump_string(value)+(" (resolved)" if is_resolved else ""))
        elif isinstance(value,bool) or isinstance(value,int):
            self.print_pair(name, str(value))
        elif isinstance(value,TypeRef):
            self.print_pair(name, value.to_string())
        elif isinstance(value,Type):
            self.print_pair(name, ("null" if value==None else value.to_string()))
        elif isinstance(value,str):
            self.print_pair(name, TextUtils.dump_string(value))
        elif isinstance(value,TypeNode):
            self.print_indent()
            self.stream.write(name+ ": " + value.type_ref()
                              + (" (resolved)" if value.is_resolved else ""))
        elif isinstance(value,Dumpable):
            self.print_indent()
            if value == None:
                self.stream.write(name+ ": null\n")
            else :
                self.stream.write(name+ ":\n")
                self.indent()
                value.dump(self)
                self.unindent()
        
    def print_pair(self,name,value):
        self.print_indent()
        self.stream.write(name + ": " + value + "\n")
    
    def indent(self):
        self.n_indent += 1
    
    def unindent(self):
        self.n_indent -= 1
    
    def print_indent(self):
        n = self.n_indent
        while n > 0:
            self.stream.write(Dumper.indent_string)
            n -= 1