class TextUtils:
    @staticmethod
    def dump_string(s,encoding="utf-8"):
        try:
            return s.encode(encoding).decode("utf-8")
        except Exception as ex:
            raise Exception("UTF-8 is not supported??: " + ex.message)

