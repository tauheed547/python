#abstraction
from abc import ABC, abstractmethod


class Appliance(ABC):
    @abstractmethod
    def turnOn(self):
        print("Turned on")
class WashingMachine(Appliance):
    print("Washing Machine")
    def turnOff(self):
        print("Turned off")
class Fridge(Appliance):
    print("Fridge")
    def turnOff(self):
        print("Turned off")
a=WashingMachine()
b=Fridge()
b.turnOn()
a.turnOn()

