class AssemblerOptions:
    def __init__(self):
        self.verbose = False
        self.args = []
    
    def add_arg(self,a):
        self.args.append(a)
