from abc import ABC, abstractmethod
from enum import nonmember


class Vehicle:
    def navigate(self):
        pass
class Car(Vehicle):
    def navigate(self):
        print("car")
class Bicycle(Vehicle):
    def navigate(self):
        print("bicycle")
for v in [Car(),Bicycle()]:
    v.navigate()
#poymorphism
class Cat:
    def make_sound(self):
        print("Meow")
class Dog(ABC):
    def make_sound(self):
        print("Bow")
for a in [Cat(),Dog()]:
    a.make_sound()

class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print("Helo")
        elif a and b:
            print("Hello hiii")
        else:
            print("huha")
puf=Demo()
puf.show(1,"",'')
#abstraction
class Cat(ABC):
    @abstractmethod
    def make_sound(self):
        print("Meow")
class Dog(ABC):
    @abstractmethod
    def make_sound(self):
        print("Bow")
for a in [Cat(),Dog()]:
    a.make_sound()

