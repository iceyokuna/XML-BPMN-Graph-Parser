from Core.CoreElement import *
from Core.IOtypes import *

class FlowObject(CoreElement):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name)
        self.inputType = inputType
        self.outputType = outputType
        self.input = None
        self.output = None
        self.flowReference = None

    def getInputType(self):
        return self.inputType

    def getOutputType(self):
        return self.outputType

    def setInput(self, Input):
        self.input = Input

    def getInput(self):
        return self.input

    def setOutput(self, output):
        self.output = output

    def getOutput(self):
        return self.output

    def setFlowReference(self, flow):
        self.flowReference = flow

    def getFlowReference(self):
        return self.flowReference