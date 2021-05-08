from abc import ABCMeta,abstractmethod

class ELFConstants(metaclass=ABCMeta):
    SectionFlag_allocatable = "a"
    SectionFlag_writable = "w"
    SectionFlag_executable = "x"
    SectionFlag_sectiongroup = "G"
    SectionFlag_strings = "S"
    SectionFlag_threadlocalstorage = "T"

    # argument of "G" flag
    Linkage_linkonce = "comdat"

    # Types
    SectionType_bits = "@progbits"
    SectionType_nobits = "@nobits"
    SectionType_note = "@note"

    SymbolType_function = "@function"