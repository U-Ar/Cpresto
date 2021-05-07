from exception.SemanticException import SemanticException
from abst.Declarations import Declarations
from exception.FileException import FileException
from WrappedParser import WrappedParser
import os

class LibraryLoader:
    @staticmethod
    def default_load_path():
        pathes = []
        pathes.append(".")
        return pathes
    
    def __init__(self,load_path=None):
        if load_path == None:
            self.load_path = ["."]
        else:
            self.load_path = load_path
        self.loading_libraries = []
        self.loaded_libraries = dict()

    def load_library(self,libid,handler):
        if libid in self.loading_libraries:
            raise SemanticException("recursive import from "+ \
                self.loading_libraries[-1]+": "+libid)
        self.loading_libraries.append(libid)
        if libid in self.loaded_libraries:
            return self.loaded_libraries[libid]
        decls = WrappedParser.parse_decl_file(self.search_library(libid),self,handler)
        self.loaded_libraries[libid] = decls
        self.loading_libraries.pop()
        return decls
    
    # returns filename of library as STRING (not File object)
    def search_library(self,libid):
        try :
            for path in self.load_path:
                filename = path + "/" + self.lib_path(libid) + ".hb"
                if os.path.exists(filename):
                    return filename
            raise FileException("no such library header file: "+libid)
        except Exception as ex:
            raise FileException(ex.message)


    def lib_path(self,ide):
        return ide.replace(".","/")
