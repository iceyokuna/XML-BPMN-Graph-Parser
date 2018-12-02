from Core.Gateway import *
import IOtypes

class ExclusiveGateway(Gateway):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name, inputType , outputType)


    #decesion making to find path
    def getPath(self):
        pass
