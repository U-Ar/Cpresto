from ConstantEntry import ConstantEntry 
class ConstantTable:
    def __init__(self):
        self.table = dict()
    
    def is_empty(self):
        return len(self.table) == 0
    
    def intern(self,s):
        if s not in self.table:
            ent = ConstantEntry(s)
            self.table[s] = ent
        return self.table[s]
    
    def entries(self):
        return list(self.table.values())
    
    #def iterator(self):
