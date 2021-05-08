from enum import Enum, auto

class Op(Enum):
    ADD = auto()
    SUB = auto()
    MUL = auto()
    S_DIV = auto()
    U_DIV = auto()
    S_MOD = auto()
    U_MOD = auto()
    BIT_AND = auto()
    BIT_OR = auto()
    BIT_XOR = auto()
    BIT_LSHIFT = auto()
    BIT_RSHIFT = auto()
    ARITH_RSHIFT = auto()

    EQ = auto()
    NEQ = auto()
    S_GT = auto()
    S_GTEQ = auto()
    S_LT = auto()
    S_LTEQ = auto()
    U_GT = auto()
    U_GTEQ = auto()
    U_LT = auto()
    U_LTEQ = auto()

    UMINUS = auto()
    BIT_NOT = auto()
    NOT = auto()

    S_CAST = auto()
    U_CAST = auto()

    @staticmethod
    def intern_binary(op,is_signed):
        if op == "+":
            return Op.ADD
        elif op == "-":
            return Op.SUB
        elif op == "*":
            return Op.MUL
        elif op == "/":
            return Op.S_DIV if is_signed else Op.U_DIV
        elif op == "%":
            return Op.S_MOD if is_signed else Op.U_MOD
        elif op == "&":
            return Op.BIT_AND
        elif op == "|":
            return Op.BIT_OR
        elif op == "^":
            return Op.BIT_XOR
        elif op == "<<":
            return Op.BIT_LSHIFT
        elif op == ">>":
            return Op.ARITH_RSHIFT if is_signed else Op.BIT_RSHIFT
        elif op == "==":
            return Op.EQ
        elif op == "!=":
            return Op.NEQ   
        elif op == "<":
            return Op.S_LT if is_signed else Op.U_LT
        elif op == "<=":
            return Op.S_LTEQ if is_signed else Op.U_LTEQ
        elif op == ">":
            return Op.S_GT if is_signed else Op.U_GT
        elif op == ">=":
            return Op.S_GTEQ if is_signed else Op.U_GTEQ 
        else:
            raise Exception("unknown binary op: "+op)
            
    @staticmethod
    def intern_unary(op):
        if op == "+":
            raise Exception("unary+ should not be in IR")
        elif op == "-":
            return Op.UMINUS
        elif op == "~":
            return Op.BIT_NOT
        elif op == "!":
            return Op.NOT
        else :
            raise Exception("unknown unary op: " + op)
