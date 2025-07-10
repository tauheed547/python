# class Product:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def getName(self):
#         print(self.name)
#         print(self.price)
# a=Product(name="tauheed",price=200)
# b=Product(name="Shaik",price=100)
# a.getName()
# b.getName()
class Marks:
    def __init__(self):
        # Private attribute
        self.__math_marks = 0

    # Method to update math marks safely
    def update_math_marks(self, marks):
        if 0 <= marks <= 100:
            self.__math_marks = marks
            print("Math marks updated successfully.")
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")

    # Method to display math marks
    def display_math_marks(self):
        print(f"Math Marks: {self.__math_marks}")


# Example usage
if __name__ == "__main__":
    student = Marks()
    student.update_math_marks(88)     # Valid
    student.display_math_marks()

    student.update_math_marks(150)    # Invalid
    student.display_math_marks()
