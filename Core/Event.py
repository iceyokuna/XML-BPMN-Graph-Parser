from Core.FlowObject import *
import IOtypes

class Event(FlowObject):
    def __init__(self , id, name, inputType , outputType ,Input ,output):
        super().__init__(id, name, inputType , outputType ,Input ,output)
        