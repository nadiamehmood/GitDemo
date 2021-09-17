# Function is a group of related statements that perform a specific task

def GreetMe(name):
    print("Hello " + name)

def Sum(a, b):
    print("{} {}".format("Sum is: ", a+b))

def Subtraction(a, b):
    return a-b

GreetMe("Nadia Mehmood")
Sum(10, 20)
print(Subtraction(20, 10))