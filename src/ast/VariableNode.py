from .LHSNode import LHSNode

class VariableNode(LHSNode):
    def __init__(self,var=None,loc=None,name=None):
        if var != None:
            self.entity = var
            self.name = var.name()
        else :
            self.entity = None
            self.name = None
        self.location = loc
        self.name = name
    
    def name(self):
        return self.name
    
    def is_resolved(self):
        return self.entity != None
    
    def entity(self):
        if self.entity == None:
            raise Exception("VariableNode.entity == None")
        return self.entity
    
    def set_entity(self,ent):
        self.entity = ent
    
    def type_node(self):
        return self.entity().type_node()
    
    def is_parameter(self):
        return self.entity().is_parameter()
    
    def orig_type(self):
        return self.entity().type()
    
    def location(self):
        return self.location

    def _dump(self,dumper):
        if self.type != None:
            dumper.print_member("type",self.type)
        else :
            dumper.print_member("name",self.name,self.is_resolved())
    
    def accept(self,visitor):
        return visitor.visit(self)