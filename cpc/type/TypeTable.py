from .VoidTypeRef import VoidTypeRef
from .VoidType import VoidType
from .IntegerType import IntegerType
from .IntegerTypeRef import IntegerTypeRef
from .UserTypeRef import UserTypeRef
from .PointerType import PointerType
from .PointerTypeRef import PointerTypeRef
from .ArrayType import ArrayType
from .ArrayTypeRef import ArrayTypeRef
from .FunctionType import FunctionType
from .FunctionTypeRef import FunctionTypeRef
from .CompositeType import CompositeType

class TypeTable:

    @classmethod
    def ilp32():
        return TypeTable.new_table(1,2,4,4,4)
    @classmethod
    def ilp64():
        return TypeTable.new_table(1,2,8,8,8)
    @classmethod
    def lp64():
        return TypeTable.new_table(1,2,4,8,8)
    @classmethod
    def llp64():
        return TypeTable.new_table(1,2,4,4,8)
    
    @classmethod
    def new_table(charsize,shortsize,intsize,longsize,ptrsize):
        table = TypeTable(intsize,longsize,ptrsize)
        table.put(VoidTypeRef(),Voidtype())
        table.put(IntegerTypeRef.char_ref(),
            IntegerType(charsize, True, "char"))
        table.put(IntegerTypeRef.short_ref(),
            IntegerType(shortsize, True, "short"))
        table.put(IntegerTypeRef.int_ref(),
            IntegerType(intsize, True, "int"))
        table.put(IntegerTypeRef.long_ref(),
            IntegerType(longsize, True, "long"))
        table.put(IntegerTypeRef.uchar_ref(),
            IntegerType(charsize, False, "unsigned char"))
        table.put(IntegerTypeRef.ushort_ref(),
            IntegerType(shortsize, False, "unsigned short"))
        table.put(IntegerTypeRef.uint_ref(),
            IntegerType(intsize, False, "unsigned int"))
        table.put(IntegerTypeRef.ulong_ref(),
            IntegerType(longsize, False, "unsigned long"))
        return table
    
    def __init__(self,intsize,longsize,ptrsize):
        self.int_size = intsize
        self.long_size = longsize
        self.pointer_size = ptrsize
        self.table = dict()

    def is_defined(self,ref):
        return ref.hash_code() in self.table
    
    def put(self,ref,t):
        if ref.hash_code() in self.table:
            raise Exception("deplicated type definition: "+ref.to_string())
        self.table[ref.hash_code()] = t
    
    def get(self,ref):
        if not (ref.hash_code() in self.table):
            if isinstance(ref,UserTypeRef):
                raise Error("undefined type: " + ref.name())
            elif isinstance(ref,PointerTypeRef):
                t = PointerType(self.pointer_size,self.get(ref.base_type()))
                self.table[ref.hash_code()] = t
                return t
            elif isinstance(ref,ArrayTypeRef):
                t = ArrayType(self.get(ref.base_type()),
                              self.pointer_size,
                              ref.length())
                self.table[ref.hash_code()] = t
                return t
            elif isinstance(ref,FunctionTypeRef):
                t = FunctionType(self.get(ref.return_type()),
                                 ref.params().intern_types(self))
                self.table[ref.hash_code()] = t
                return t
            raise Exception("unregistered type: " + ref.to_string())
        else:
            return self.table[ref.hash_code()]

    def get_param_type(self,ref):
        t = self.get(ref)
        if t.is_array():
            return self.pointer_to(t.base_type())
        return t
    
    def int_size(self):
        return self.int_size
    def long_size(self):
        return self.long_size
    def pointer_size(self):
        return self.pointer_size
    def max_int_size(self):
        return self.pointer_size
    def ptr_diff_type(self):
        return self.get(self.ptr_diff_type_ref())
    #returns a IntegerTypeRef whose size equals to pointer
    def ptr_diff_type_ref(self):
        return IntegerTypeRef(self.ptr_diff_type_name())
    def ptr_diff_type_name(self):
        if (self.signed_long().size() == self.pointer_size):
            return "long"
        if (self.signed_int().size() == self.pointer_size):
            return "int"
        if (self.signed_short().size() == self.pointer_size):
            return "short"
        raise Exception("must not happen: integer.size != pointer.size")

    def signed_stack_type(self):
        return self.signed_long()
    
    def unsigned_stack_type(self):
        return self.unsigned_long()
    
    def types(self):
        return list(self.table.values())
    
    def void_type(self):
        return self.table.get(VoidTypeRef())
    
    def signed_char(self):
        return self.table.get(IntegerTypeRef.char_ref())
    def signed_short(self):
        return self.table.get(IntegerTypeRef.short_ref())
    def signed_int(self):
        return self.table.get(IntegerTypeRef.int_ref())
    def signed_long(self):
        return self.table.get(IntegerTypeRef.long_ref())
    def unsigned_char(self):
        return self.table.get(IntegerTypeRef.uchar_ref())
    def unsigned_short(self):
        return self.table.get(IntegerTypeRef.ushort_ref())
    def unsigned_int(self):
        return self.table.get(IntegerTypeRef.uint_ref())
    def unsigned_long(self):
        return self.table.get(IntegerTypeRef.ulong_ref())

    def pointer_to(self,base_type):
        return PointerType(self.pointer_size,base_type)
    
    def semantic_check(self,h):
        for t in self.types():
            if isinstance(t,CompositeType):
                self.check_void_members(t,h)
                self.check_duplicated_members(t,h)
            elif isinstance(t,ArrayType):
                self.check_void_members(t,h)
            self.check_recursive_definition(t,h)

    def check_void_members(self,t,h):
        if isinstance(t,ArrayType):
            if t.base_type().is_void():
                h.error("array cannot contain void")
        else :
            for s in t.members():
                if s.type().is_void():
                    h.error("struct/union cannot contain void",t.location())
    
    def check_duplicated_members(self,t,h):
        seen = dict()
        for s in t.members():
            if s.name() in seen:
                h.error(t.to_string()+" has duplicated member: " + s.name(),
                        t.location())
            seen[s.name()] = s
    
    def check_recursive_definition(self,t,h):
        d = dict()
        self._check_recursive_definition(t,d,h)
    
    checking = 1
    checked  = 2

    def _check_recursive_definition(self,t,marks,h):
        key = t.to_string()
        if key not in marks:
            marks[key] = TypeTable.checking
            if isinstance(t,CompositeType):
                for s in t.members():
                    self._check_recursive_definition(s.type(),marks,h)
            elif isinstance(t,ArrayType):
                self._check_recursive_definition(t.base_type(),marks,h)
            elif isinstance(t,UserType):
                self._check_recursive_definition(t.real_type(),marks,h)
            marks[key] = TypeTable.checked
        elif marks[key] == TypeTable.checking:
            h.error("recursive type definition: "+key,t.location())
            return
        elif marks[key] == TypeTable.checked:
            return
        




    
    


    