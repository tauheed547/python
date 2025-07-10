from tkinter.font import names


class Student:
    def __init__(self,name,marks):
        self.__name=name
        self.__marks=marks
    def set_name(self):
        self.__name=self.__name
    def get_name(self):
        return self.__name
    def set_marks(self):
        self.__marks=self.__marks
    def get_marks(self):
        if self.__marks >= 0 and self.__marks <= 100:
            return self.__marks
        else:
            print("Invalid marks")
name=input("Enter your name: ")
marks=int(input("Enter your marks: "))
var=Student(name,marks)
print("Student Marks: ",var.get_marks())