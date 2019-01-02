from Core.ServiceTask import ServiceTask
from Core.UserTask import UserTask
from Core.StartEvent import StartEvent
from Core.EndEvent import EndEvent
from Core.ExclusiveGateway import ExclusiveGateway
from Core.SequenceFlow import SequenceFlow
from Core.IOtypes import *

class BPMNEngine:
    def __init__(self):
        self.startEvent = None
        self.elements = {}
        self.currentExecution = None
        self.countTask = 0

    def addStartEvent(self, Id, name):
        startEvent = StartEvent(Id, name, None, None)
        self.startEvent = startEvent
        self.elements[Id] = startEvent
        self.currentExecution = self.startEvent

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

    #connect Tasks, Gateways only still not support other coreElements
    def connect(self, sourceId, flowId, targetId):
        sequencialFlow = self.elements[flowId]
        sourceElement = self.elements[sourceId]
        targetElement = self.elements[targetId]
        
        sequencialFlow.setSource(sourceElement)
        sequencialFlow.setTarget(targetElement)
        
        sourceElement.setFlowReference(sequencialFlow)
        
    def start(self):
        print("startExecution")

    def next(self):
        connectedFlow = self.currentExecution.getFlowReference()
        self.currentExecution = connectedFlow.getTarget()

    #to use input and call service
    def perform(self):
        print(self.currentExecution)
        

if __name__ == "__main__":
    bpmn = BPMNEngine()
    bpmn.addStartEvent(1,'start')
    bpmn.addUserTask(2,'usertask1',None,None)
    bpmn.addSequenceFlow(5,'flow1')
    bpmn.addServiceTask(3,'servicetask1',None,None)
    bpmn.addServiceTask(4,'servicetask2',None,None)
    bpmn.addSequenceFlow(6,'flow2')
    bpmn.addExclusiveGateway(7,'gateway',None,None)
    bpmn.addSequenceFlow(8,'flow3')
    bpmn.addSequenceFlow(9,'flow4')
    bpmn.connect(1,5,2)
    bpmn.connect(2,6,7)
    bpmn.connect(7,8,3)
    bpmn.connect(7,8,4)



##>>> data = '{"researcher": {"name": "Ford Prefect","species": "Betelgeusian","relatives": [{"name": "Zaphod Beeblebrox","species": "Betelgeusian"}]}}'
##>>> data  = json.loads(data)
##>>> for i in data:
##	print(data[i])

    
