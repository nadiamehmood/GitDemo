
str = "www.google.com"
str1 = "Search Engine"
str3 = "google"

print("Second index of str: "+ str[1])
print("Concatenation of 2 strings: "+ str + str1)
print("{} {}".format("Is 'google' is present in 'www.google.com'", str3 in str))   # substring check

value = str.split(".")
print(value)    # ['www', 'google', 'com']
print(value[1])

str4 = " good "
print(str4.strip())    #good
print(str4.lstrip())   #good
print(str4.rstrip())   # good