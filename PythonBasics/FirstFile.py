print("hello")

a, b, c = 10, 12.3, "Hello"

# concatenate 2 different datatypes
print("{}: {}, {} and {}".format("Value of a b and c is", a, b, c))

print(type(a))
print(type(b))
print(type(c))

#List Datatypes == Not Immutable which means we can change the existing behavior
values = [10, 30, "Nadia", 14, 9]

print(values[0]) #print 10
print(values[3]) #print 14
print(values[-1]) #print 9
print(values[1:4]) #prints 30, Nadia, 14
values.insert(3, "Mehmood")
print(values)  #[10, 30, 'Nadia', 'Mehmood', 14, 9]
values.append("End") #it will append at the last index
print(values)  #[10, 30, 'Nadia', 'Mehmood', 14, 9, 'End']
values[4] = 15 #Updating
print(values) #[10, 30, 'Nadia', 'Mehmood', 15, 9, 'End']
del values[0]
print(values) #[30, 'Nadia', 'Mehmood', 15, 9, 'End']

# Tuple ==> Immutable means when you declare the tuple you cannot update it again
tuple = (89, "Ali", 100, 55)
print(tuple[1])
# tuple[1] = "Nadia"  # throws an error ""

# Dictionary ==> Key value pairs
dic = {"a": 3, 4: "Ahmed", "c": "Nadia"}
print(dic["a"])
print(dic[4])

# Create dictionary dynamically
dict = {}

dict["firstname"] = "Nadia"
dict["lastname"] = "Mehmood"
dict["gender"] = "Female"
print(dict)
print(dict["firstname"])

# if else
greetings = "Good Morning"
a = 8

if a > 4:                      # greetings == "Morning"
    print("condition matches")
else:
    print("Condition do not match")
print("if else code ended")

# For loop
obj = [1, 2, 4, 5, 6, 7]

for i in obj:
    print(i)

# multiples of 2
for i in obj:
    print(i*2)

# when we define range in loop
summation = 0
for j in range(1, 6):
    summation = summation + j
    print(summation)

# adding iteration in range
for k in range(1, 10, 2):         # 1, 3, 5, 7, 9
    print(k)

# only 1 argument and it will consider it maximum argument and start value would be 0
for m in range(10):         # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(m)

# While loop with Break and Continue Statement
print("While loop with Break and Continue Statement")
it = 9
while it < 16:
    if it == 13:
        it = it + 1
        continue    # It will only skip current iteration
    if it == 15:
        break     # it will break the entire loop
    print(it)
    it = it + 1


print("hello word")
print("hello word")
print("hello word")
print("hello word")
print("hello word")

print("hello word")
print("hello word")
