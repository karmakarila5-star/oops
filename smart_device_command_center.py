from abc import ABC, abstractmethod

class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name
        self.is_on = False

    @abstractmethod
    def activate(self):
        pass

class SmartLight(SmartDevice):
    def activate(self):
        self.is_on = True
        print(self.name + " turned on")

class Smartheating(SmartDevice):
    def activate(self):
        self.is_on = True
        print(self.name + " heating up!")

devices = [SmartLight("Light"), Smartheating("light")]

for d in devices:
    d.activate()