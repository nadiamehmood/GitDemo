# self keyword is mandatory for calling variable names into methods
class Calculator:
    num = 100  # Class variables -> Declare inside the class

    # Default Constructor / Parameterized constructor
    def __init__(self, a, b):
        self.firstNum = a           # instance variable that declare only in constructor and its value keeps on changing while object creation
        self.secondNum = b
        print("I am called automatically when the object is created")

    def getData(self):
        print("Class method called")

    def summation(self):
        return self.firstNum + self.secondNum + Calculator.num + self.num   # how to access class variables

obj = Calculator(10, 20)
obj.getData()
print(obj.num)
print("{} {}".format("Sum of object 1 is: ", obj.summation()))

obj1 = Calculator(50, 50)
obj1.getData()
print(obj1.num)
print("{} {}".format("Sum of object 2 is: ", obj1.summation()))