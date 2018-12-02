from Core.FlowObject import *
import IOtypes

class Gateway(FlowObject):
    def __init__(self , id, name):
        super().__init__(id, name)
        self.inputType = None
        self.outputType = None
        self.input = None
        self.output = None

    def getInputType(self):
        return self.inputType

    def getOutputType(self):
        return self.outputType
