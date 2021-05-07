from .LHSNode import LHSNode

class VariableNode(LHSNode):
    def __init__(self,var=None,loc=None,name=None):
        if var != None:
            self._entity = var
            self._name = var.name()
        else :
            self._entity = None
            self._name = None
        self._location = loc
        self._name = name
    
    def name(self):
        return self._name
    
    def is_resolved(self):
        return self._entity != None
    
    def entity(self):
        if self._entity == None:
            raise Exception("VariableNode.entity == None")
        return self._entity
    
    def set_entity(self,ent):
        self._entity = ent
    
    def type_node(self):
        return self._entity.type_node()
    
    def is_parameter(self):
        return self._entity.is_parameter()
    
    def orig_type(self):
        return self._entity.type()
    
    def location(self):
        return self._location

    def _dump(self,dumper):
        if self.type != None:
            dumper.print_member("type",self.type())
        else :
            dumper.print_member("name",self._name,self.is_resolved())
    
    def accept(self,visitor):
        return visitor.visit(self)