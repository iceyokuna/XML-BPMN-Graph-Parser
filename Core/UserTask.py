from Core.Activity import *
import IOtypes

class UserTask(CoreElement):
    def __init__(self , id, name):
        super().__init__(id, name)
        self.HTMLReference = None
        self.inputType = None
        self.outputType = None
        self.input = None
        self.output = None

    def getHTML(self):
        pass

    def getInputType(self):
        return self.inputType

    def getOutputType(self):
        return self.outputType

    def start(self,Input):
        self.input = Input

    def setOutput(self,output):
        self.output = output
    
    def end(self):
        return self.output
