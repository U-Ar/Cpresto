class Statistics :
    def __init__(self):
        self.register_usage = dict()
        self.insn_usage = dict()
        self.symbol_usage = dict()
    
    @staticmethod
    def collect(assemblies):
        stats = Statistics()
        for a in assemblies:
            a.collect_statistics(stats)
        return stats
    
    def does_register_used(self,reg):
        return self.num_register_used(reg) > 0
    
    def num_register_used(self,reg):
        return self.fetch_count(self.register_usage,reg)
    
    def register_used(self,reg):
        self.increment_count(self.register_usage,reg)
    
    def num_instruction_usage(self,insn):
        return self.fetch_count(self.insn_usage,insn)
    
    def instruction_used(self,insn):
        self.increment_count(self.insn_usage,insn)
    
    def does_symbol_used(self,label):
        if isinstance(label,Label):
            return self.num_symbol_used(label.symbol()) > 0
        else :
            return self.num_symbol_used(label) > 0
    
    def num_symbol_used(self,sym):
        return self.fetch_count(self.symbol_usage,sym)
    
    def symbol_used(self,sym):
        self.increment_count(self.symbol_usage,sym)
    
    def fetch_count(self,m,key):
        if key not in m:
            return 0
        else :
            return m[key]
        
    def increment_count(self,m,key):
        m[key] = self.fetch_count(m,key) + 1
    