from Core.CoreElement import *
import IOtypes

class FlowObject(CoreElement):
    def __init__(self , id, name, inputType , outputType ,Input ,output):
        super().__init__(id, name)
        self.inputType = inputType
        self.outputType = outputType
        self.input = Input
        self.output = output

    def getInputType(self):
        return self.inputType

    def getOutputType(self):
        return self.outputType

