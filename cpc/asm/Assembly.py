from abc import ABCMeta, abstractmethod

class Assembly(metaclass=ABCMeta):
    @abstractmethod
    def to_source(self,table):
        pass
    @abstractmethod
    def dump(self):
        pass

    def is_instruction(self):
        return False
    
    def is_label(self):
        return False
    
    def is_directive(self):
        return False
    
    def is_comment(self):
        return False

    def collect_statistics(self,stats):
        # does nothing by default
        pass