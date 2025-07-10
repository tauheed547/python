class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b=b
    #addition
    def addition(self):
        return self.a+self.b
    #subtraction
    def subtraction(self):
        return self.a-self.b
    #multiplication
    def multiplication(self):
        return self.a*self.b
    #division
    def division(self):
        if self.a>=0:
            return self.a/self.b
        else:
            print("Not Defdined")
var1=int(input("Enter first number: "))
var2=int(input("Enter second number: "))
var=Calculator(var1,var2)
print(var.addition())
print(var.subtraction())
print(var.multiplication())
print(var.division())