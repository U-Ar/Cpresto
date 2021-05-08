from abc import ABCMeta,abstractmethod

class Linker(metaclass=ABCMeta):
    @abstractmethod
    def generate_executable(self,args,destpath,opts):
        pass

    @abstractmethod
    def generate_shared_library(self,args,destpath,opts):
        pass