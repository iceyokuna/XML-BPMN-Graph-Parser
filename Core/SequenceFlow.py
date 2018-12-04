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

    def getCondition(self):
        self.conditionExpression

    #return boolean check condition flow
    def checkCondition(self, Input):
        if(Input == self.conditionExpression):
            return True
        return False