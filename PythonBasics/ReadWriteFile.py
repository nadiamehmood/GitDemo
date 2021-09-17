# file = open('TextFile')
# Read all text from file
#print(file.read(5)) # prints start
#print(file.readline())
#print(file.readline())

# print all file record line by line by using readline method
# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

# readlines -> creates a list of file
# for line in file.readlines():
#     print(line)

# file.close()

with open('TextFile', 'r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('TextFile', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
