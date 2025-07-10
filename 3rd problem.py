class Employee:
    def __init__(self,name,salary,age):
        self.__name=name
        self.__salary=salary
        self.__age=age
    def set_name(self):
        self.__name=self.__name
    def get_name(self):
        return self.__name
    def set_salary(self):
        self.__salary=self.__salary
    def get_salary(self):
        if self.__salary > 0:
            return self.__salary
        else:
            print("Salary must be greater then Zero")
    def set_age(self):
        self.__age=self.__age
    def get_age(self):
        if self.__age >= 18 and self.__age <= 100:
            return self.__age
        else:
            print("Invalid")
name=input("Enter your name: ")
salary=int(input("Enter your salary: "))
age=int(input("Enter your age: "))
var=Employee(name,salary,age)
print("Salary: ",var.get_salary())