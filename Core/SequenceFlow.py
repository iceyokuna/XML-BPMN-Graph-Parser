from Core.ConnectingObject import *

class SequenceFlow(ConnectingObject):
    def __init__(self,  id, name):
        super().__init__(id, name)
        self.InputType = None
        self.Input = None
        self.conditionType = None
        self.conditionExpression = None

    def setCondition(self, conditionTyes, condition):
        self.conditionType = conditionTyes
        self.conditionExpression = condition

    #return boolean check condition flow
    def checkFlow(self, Input):
        pass

