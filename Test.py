from Core.ServiceTask import ServiceTask
from Core.StartEvent import StartEvent
from Core.EndEvent import EndEvent
from Core.ExclusiveGateway import ExclusiveGateway
from Core.SequenceFlow import SequenceFlow
from Core.IOtypes import *

class BPMNEngine:
    def __init__(self):
        self.startEvent = None
        self.elements = {}

    def addStartEvent(self, Id, name):
        startEvent = StartEvent(Id, name, None, None)
        self.elements[Id] = startEvent

    def addUserTask(self, Id, name, inputType, outputType):
        newUserTask = UserTask(Id, name, inputType, outputType)
        self.elements[Id] = newUserTask

    def addServiceTask(self, Id, name, inputType, outputType):
        newServiceTask = ServiceTask(Id, name, inputType, outputType)
        self.elements[Id] = newServiceTask

    def addExclusiveGateway(self, Id, name, inputType, outputType):
        newExclusiveGateway = ServiceTask(Id, name, inputType, outputType)
        self.elements[Id] = newExclusiveGateway

    def addSequenceFlow(self, Id, name):
        newSequenceFlow = SequenceFlow(Id, name)
        self.elements[Id] = newSequenceFlow

    def addEndEvent(self, Id, name):
        endEvent = EndEvent(Id, name, None, None)
        self.elements[Id] = endEvent

    def connect(self, sourceId, flowId, targetId):
        pass

    def start(self):
        pass

    def next(self):
        pass


