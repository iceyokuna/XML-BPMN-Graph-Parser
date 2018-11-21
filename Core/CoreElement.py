from abc import ABC, abstractmethod

class CoreElement(ABC):
    def __init__(self, elementId, elementName):
        self.id = elementId
        self.name = elementName

    @abstractmethod
    def perform(self):
        pass
