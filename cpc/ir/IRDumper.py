import asm.Type.Type
import type.Type.Type

class IRDumper:
    def __init__(self,s):
        self.stream = s
        self.num_indent = 0

    def print_class(self,obj,loc=None):
        self.print_indent()
        if loc == None:
            self.stream.write("<<"+type(obj).__name__ + ">>\n")
        else :
            self.stream.write("<<"+type(obj).__name__ + ">> ("+ loc.to_string() +")\n")
    
    def print_member(self,name,memb):
        if isinstance(memb,int):
            self.print_pair(name, str(memb))
        elif isinstance(memb,bool):
            self.print_pair(name, str(memb))
        elif isinstance(memb,str):
            self.print_pair(name, memb)
        elif isinstance(memb,Label):
            self.print_pair(name, str(type(memb)))
        elif isinstance(memb,asm.Type.Type):
            self.print_pair(name, memb.to_string())
        elif isinstance(memb,type.Type.Type):
            self.print_pair(name, memb.to_string())  
        elif isinstance(memb,IRDumpable):
            self.print_indent()
            if memb == None:
                self.stream.write(name+": None\n")
            else:
                self.stream.write(name+":\n")
                self.indent()
                memb.dump(self)
                self.unindent()

    def print_members(self,name,elems):
        self.print_indent()
        self.stream.write(name+ ":\n")
        self.indent()
        for elem in elems:
            elem.dump(self)
        self.unindent()
    
    def print_vars(self,name,vs):
        self.print_indent()
        self.stream.write(name+ ":\n")
        self.indent()
        for var in vs:
            self.print_class(var,vs.location)
            self.print_member("name",var.name)
            self.print_member("is_private",var.is_private())
            self.print_member("type",var.type())
            self.print_member("initializer",var.ir)
        self.unindent()
    
    def print_funcs(self,name,funcs):
        self.print_indent()
        self.stream.write(name+ ":\n")
        self.indent()
        for f in funcs:
            self.print_class(f,f.location)
            self.print_member("name",f.name)
            self.print_member("is_private",f.is_private())
            self.print_member("type",f.type())
            self.print_member("body",f.ir)
        self.unindent()

    def print_pair(self,name,value):
        self.print_indent()
        self.stream.write(name+": "+value+"\n")

    def indent(self):
        self.num_indent += 1
    def unindent(self):
        self.num_indent -= 1
    indent_string = "    "

    def print_indent(self):
        n = self.num_indent
        while n > 0:
            self.stream.write(IRDumper.indent_string)
            n -= 1