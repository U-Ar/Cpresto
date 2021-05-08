class LinkerOptions:
    def __init__(self):
        self.generating_shared_library = False
        self.generating_PIE = False
        self.no_start_files = False
        self.no_default_libs = False
        self.verbose = False