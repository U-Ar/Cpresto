class CodeGeneratorOptions:
    def __init__(self):
        self._optimize_level = 0
        self._generate_PIC = False
        self._generate_PIE = False
        self._verbose_asm = False

    def set_optimization_level(self,level):
        self.optimize_level = level
    
    def optimize_level(self):
        return self._optimize_level
    
    def generate_verbose_asm(self):
        self._verbose_asm = True
    
    def is_verbose_asm(self):
        return self._verbose_asm
    
    def is_position_independent(self):
        return self._generate_PIC or self._generate_PIE
    
    def generate_PIC(self):
        self._generate_PIC = True
    
    def is_PIC_required(self):
        return self._generate_PIC
    
    def generate_PIE(self):
        self._generate_PIE = True
    
    def is_PIE_required(self):
        return self._generate_PIE