from abc import ABC, abstractmethod

# Abstraction
class Vehicle(ABC):
    def __init__(self, brand, fuel_capacity, mileage):
        self.__brand = brand
        self.__fuel_capacity = fuel_capacity
        self.__mileage = mileage
        self.__fuel = 0
        self.__km_run = 0

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    # Encapsulation
    def refuel(self, liters):
        if self.__fuel + liters > self.__fuel_capacity:
            print(f"{self.__brand}: Cannot refuel beyond fuel capacity.")
        else:
            self.__fuel += liters
            print(f"{self.__brand}: Refueled {liters}L. Current fuel: {self.__fuel}L")

    def drive(self, km):
        fuel_needed = km / self.__mileage
        if self.__fuel >= fuel_needed:
            self.__fuel -= fuel_needed
            self.__km_run += km
            print(f"{self.__brand}: Trip of {km} km completed.")
        else:
            print(f"{self.__brand}: Not enough fuel for trip.")

    def summary(self):
        print(f"{self.__class__.__name__} - Brand: {self.__brand}, Fuel: {self.__fuel}L, KM Run: {self.__km_run}")
        print(f"{self.__brand} is a {self.__class__.__name__}")
        print("Needs Service" if self.__km_run > 10000 else "Does Not Need Service")
        print()

# Inheritance and Polymorphism
class Car(Vehicle):
    def start(self):
        print(f"{self._Vehicle__brand} Car is starting...")

    def stop(self):
        print(f"{self._Vehicle__brand} Car is stopping...")

class Bike(Vehicle):
    def start(self):
        print(f"{self._Vehicle__brand} Bike is starting...")

    def stop(self):
        print(f"{self._Vehicle__brand} Bike is stopping...")

class Truck(Vehicle):
    def start(self):
        print(f"{self._Vehicle__brand} Truck is starting...")

    def stop(self):
        print(f"{self._Vehicle__brand} Truck is stopping...")

# 🧪 Object Creation and Actions
car = Car("Toyota", 50, 10.6)
bike = Bike("Yamaha", 10, 40)
truck = Truck("Volvo", 100, 20)

# Car Actions
car.start()
car.refuel(30)
car.drive(200)
car.summary()
car.stop()

# Bike Actions
bike.start()
bike.refuel(30)  # Should trigger refuel limit
bike.summary()
bike.stop()

# Truck Actions
truck.start()
truck.refuel(30)
truck.drive(200)
truck.summary()
truck.stop()

# Fleet Summary
print("=== Fleet Summary ===")
car._Vehicle__km_run += 10000  # simulate long-term mileage
for vehicle in [car, bike, truck]:
    vehicle.summary()