from Core.Event import *
from Core.IOtypes import *

class EndEvent(Event):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name, inputType , outputType)
        