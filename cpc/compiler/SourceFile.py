from LdArg import LdArg
import os

class SourceFile(LdArg):
    EXT_CPRESTO_SOURCE = ".cb"
    EXT_ASSEMBLY_SOURCE = ".s"
    EXT_OBJECT_FILE = ".o"
    EXT_STATIC_LIBRARY = ".a"
    EXT_SHARED_LIBRARY = ".so"
    EXT_EXECUTABLE_FILE = ""

    KNOWN_EXTENSIONS = [
        SourceFile.EXT_CPRESTO_SOURCE,
        SourceFile.EXT_ASSEMBLY_SOURCE,
        SourceFile.EXT_OBJECT_FILE,
        SourceFile.EXT_STATIC_LIBRARY,
        SourceFile.EXT_SHARED_LIBRARY,
        SourceFile.EXT_EXECUTABLE_FILE
    ]

    def __init__(self,name):
        self.original_name = name
        self.current_name = name
    
    def is_source_file(self):
        return True
    
    def to_string(self):
        return self.current_name

    def path(self):
        return self.current_name
    
    def current_name(self):
        return self.current_name
    
    def set_current_name(self,name):
        self.current_name = name
    
    def is_known_file_type(self):
        ext = self.ext_name(self.original_name)
        for e in SourceFile.KNOWN_EXTENSIONS:
            if e == ext:
                return True
        return False
    
    def is_Cpresto_source(self):
        return self.ext_name(self.current_name) == SourceFile.EXT_CPRESTO_SOURCE
    def is_assembly_source(self):
        return self.ext_name(self.current_name) == SourceFile.EXT_ASSEMBLY_SOURCE
    def is_object_file(self):
        return self.ext_name(self.current_name) == SourceFile.EXT_OBJECT_FILE
    def is_shared_library(self):
        return self.ext_name(self.current_name) == SourceFile.EXT_SHARED_LIBRARY
    def is_static_library(self):
        return self.ext_name(self.current_name) == SourceFile.EXT_STATIC_LIBRARY
    def is_executable(self):
        return self.ext_name(self.current_name) == SourceFile.EXT_EXECUTABLE_FILE
    
    def asm_file_name(self):
        return self.replace_ext(SourceFile.EXT_ASSEMBLY_SOURCE)
    def obj_file_name(self):
        return self.replace_ext(SourceFile.EXT_OBJECT_FILE)
    def linked_file_name(self,new_ext):
        return self.replace_ext(new_ext)
    
    def replace_ext(self,ext):
        return self.base_name(self.original_name,True) + ext
    
    def base_name(self,path,strip_ext=None):
        if strip_ext == None or strip_ext == False:
            return os.path.basename(path)
        elif 
            return os.path.splitext(os.path.basename(path))[0]
    
    def ext_name(self,path):
        return os.path.splitext(path)[1]

