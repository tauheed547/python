#Abstraction
from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def Start(self):
        print(f"{brand} car is starting")
    @abstractmethod
    def stop(self):
        print("Car is stopping...")
class Car(vehicle):
    def __init__(self,fuel_capacity,mileage):
        self.__fuel_capacity=fuel_capacity
        self.__mileage=mileage
    def Start(self):
        print("Start")
    def stop(self):
        print("Stop")
    def set_fuel_capacity(self,fuel_capacity):
        self.__fuel_capacity=fuel_capacity
    def get_fuel_capacity(self):
        return self.__fuel_capacity
    def display_info(self):
        print("Toyoto car is stopping")
    # self.__fuel=self.__fuel

class Bike(vehicle):
    print("Yamaha Bike is starting")
    print("Bike Brand: Yamaha")
    def __init__(self,fuel_capacity,mileage):
        self.__fuel_capacity=fuel_capacity
        self.__mileage=mileage
    def Start(self):
        print("Start")
    def stop(self):
        print("Stop")
    def set_fuel_capacity(self,fuel_capacity):
        self.__fuel_capacity=fuel_capacity
    def get_fuel_capacity(self):
        return self.__fuel_capacity
    def display_info(self):
        print("Yamaha Bike is stopping")
brand=input("car Brand:")
fuel_capacity=int(input("Enter Fuel Capacity:"))
mileage=int(input("Enter Mileage:"))
car=Car(mileage,fuel_capacity)
bike=Bike(mileage,fuel_capacity)

