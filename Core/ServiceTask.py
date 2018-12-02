from Core.Activity import *
from Core.IOtypes import *

class ServiceTask(Activity):
    def __init__(self , id, name, inputType , outputType):
        super().__init__(id, name, inputType , outputType)
        self.HTMLReference = None
        self.serviceURL=  None

    def setURL(self,url):
        self.serviceURL = url
    
    def getURL(self):
        return self.serviceURL

    def getHTML(self):
        return self.HTMLReference

    #perform service
    def perform(self):
        pass
