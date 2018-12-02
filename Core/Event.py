from Core.FlowObject import *
from Core.IOtypes import *

class Event(FlowObject):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name, inputType , outputType)
        