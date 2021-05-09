from abc import ABCMeta,abstractmethod

class ELFConstants(metaclass=ABCMeta):
    section_flag_allocatable = "a"
    section_flag_writable = "w"
    section_flag_executable = "x"
    section_flag_sectiongroup = "G"
    section_flag_strings = "S"
    section_flag_threadlocalstorage = "T"

    # argument of "G" flag
    linkage_linkonce = "comdat"

    # Types
    section_type_bits = "@progbits"
    section_type_nobits = "@nobits"
    section_type_note = "@note"

    symbol_type_function = "@function"