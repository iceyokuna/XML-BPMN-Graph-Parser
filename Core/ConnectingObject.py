from Core.CoreElement import *

class ConnectingObject(CoreElement):
    def __init__(self , id, name):
        super().__init__(id, name)
        self.sourceReference = None
        self.targetReference = None

    def setSource(self, source):
        self.sourceReference = source

    def setTarget(self, target):
        self.targetReference = target

    def getSource(self):
        return self.sourceReference

    def getTarget(self):
        return self.targetReference
