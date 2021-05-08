from .Symbol import Symbol

class BaseSymbol(Symbol):
    def __init__(self):
        super().__init__()

    def is_zero(self):
        return False
    
    def collect_statistics(self,stats):
        stats.symbol_used(self)
    
    def plus(self,n):
        raise Exception("must not happen: BaseSymbol.plus called")