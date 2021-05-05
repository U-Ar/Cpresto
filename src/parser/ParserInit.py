def parser_init(s,name,loader,error_handler,debug=None):
    parser = CprestoParser(s)
    parser.source_name = name
    parser.loader = loader
    parser.error_handler = error_handler
    parser.known_typedefs = dict()
    return parser