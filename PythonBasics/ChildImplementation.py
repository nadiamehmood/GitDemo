# Constructor which is not default in parent class, should be called in child constructor
from PythonBasics.OopsDemo import Calculator

class ChildImplementation(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 1)  # Call parameterized constructor

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = ChildImplementation()
print("{} {}".format("Complete value from child class: ", obj.getCompleteData()))

print("hello word")
print("hello word")
print("hello word")
print("hello word")

print("new")