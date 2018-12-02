from Core.CoreElement import *

class ConnectingObject(CoreElement):
    def __init__(self , id, name):
        super().__init__(id, name)
        self.sourceReference = None
        self.targetReference = None

    def getSource(self):
        return self.sourceReference

    def getTarget(self):
        return self.targetReference
