from Core.CoreElement import *

class Task(CoreElement):
    def __init__(self , task_id, task_name, ):
        super().__init__(task_id, task_name)
        self.service_obj = None
        self.flow = None

    def perform(self):
        pass
