from enum import Enum

class Type:
    INT8 = 0
    INT16 = 1
    INT32 = 2
    INT64 = 3

    @staticmethod
    def get(size):
        if size == Type.INT8.value:
            return Type.INT8
        elif size == Type.INT16.value:
            return Type.INT16
        elif size == Type.INT32.value:
            return Type.INT32
        elif size == Type.INT64.value:
            return Type.INT64
        else :
            raise Exception("unsupported asm type size: " + str(size))

    def size(self):
        if self.value == Type.INT8.value:
            return 1
        elif self.value == Type.INT16.value:
            return 2
        elif self.value == Type.INT32.value:
            return 4
        elif self.value == Type.INT64.value:
            return 8
        else :
            raise Exception("must not happen")