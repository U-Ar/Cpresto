class AsmUtils:
    def __init__(self):
        pass

    @classmethod
    def align(n,alignment):
        return ((n+alignment-1)//alignment) * alignment