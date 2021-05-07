from .TypeRef import TypeRef

class IntegerTypeRef(TypeRef):
    @staticmethod
    def char_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("char")
        return IntegerTypeRef("char",loc)

    @staticmethod
    def short_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("short")
        return IntegerTypeRef("short",loc)
    
    @staticmethod
    def int_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("int")
        return IntegerTypeRef("int",loc)
    
    @staticmethod
    def long_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("long")
        return IntegerTypeRef("long",loc)

    @staticmethod
    def uchar_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("unsigned char")
        return IntegerTypeRef("unsigned char",loc)

    @staticmethod
    def ushort_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("unsigned short")
        return IntegerTypeRef("unsigned short",loc)

    @staticmethod
    def uint_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("unsigned int")
        return IntegerTypeRef("unsigned int",loc)
    
    @staticmethod
    def ulong_ref(loc=None):
        if loc == None:
            return IntegerTypeRef("unsigned long")
        return IntegerTypeRef("unsigned long",loc)

    def __init__(self,name,loc=None):
        super().__init__(loc)
        self.name = name
    
    def name(self):
        return self.name

    def equals(self,other):
        if not isinstance(other,IntegerTypeRef):
            return False
        return self.name == other.name()
    
    def to_string(self):
        return self.name
    
