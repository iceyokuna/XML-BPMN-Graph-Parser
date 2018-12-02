from Core.FlowObject import *
from Core.IOtypes import *

class Gateway(FlowObject):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name, inputType , outputType)
        self.flowReferenceList = []

    def addFlow(self, flow):
        self.flowReferenceList.append(flow)

    def getFlow(self):
        return self.flowReferenceList
