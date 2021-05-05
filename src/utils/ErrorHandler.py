import sys

class ErrorHandler:
    def __init__(self,progid,stream=None):
        if stream == None:
            self.stream = sys.stderr
        else:
            self.stream = stream
        self.program_id = progid
        self.n_error = 0
        self.n_warning = 0
    
    def error(self,msg,loc=None):
        if loc == None:
            self.stream.write(self.program_id+": error: "+msg+"\n")
            self.n_error += 1
        else :
            self.stream.write(self.program_id+": error: "+loc.to_string()+": "+msg+"\n")
            self.n_error += 1
        
    def warn(self,msg,loc=None):
        if loc == None:
            self.stream.write(self.program_id+": warning: "+msg+"\n")
            self.n_warning += 1
        else :
            self.stream.write(self.program_id+": warning: "+loc.to_string()+": "+msg+"\n")
            self.n_warning += 1
    
    def error_occured(self):
        return self.n_error > 0