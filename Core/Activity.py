from Core.FlowObject import *
import IOtypes

class Activity(FlowObject):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name, inputType , outputType)
