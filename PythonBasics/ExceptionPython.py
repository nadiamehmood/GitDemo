
# ItemsInCart = 0
# if ItemsInCart != 2: #raise Exception("Products cart count not matched")
#     pass
#
# assert(ItemsInCart == 2)

# Try , Catch
try:
    with open('textFile', 'r') as reader:
        reader.read()

except:
    print("Some how i reached this block when there is failure in try block")    # custom exception

try:
    with open('textFile', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)     # Error thrown by python interpreter

finally:
    print("Clean up all records or cookies by end of the code")
