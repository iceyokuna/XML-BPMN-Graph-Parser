from Core.Gateway import *
from Core.IOtypes import *

class ExclusiveGateway(Gateway):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name, inputType , outputType)

    #Overiding 
    def getFlowReference(self):
        selectedFlow = None
        for flow in self.flowReferenceList:
            target = flow.getTarget()
            if(self.inputType == target.getOutputType()):
                if(flow.checkCondition(self.input)):
                    return flow
        #return default flow
        return self.flowReferenceList[0]
