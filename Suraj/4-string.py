mystr = "surASDFMSAPNGIAGPDajis a good boy"
# b = input("Enter your first name")
# print(b.capitalize())
# c = input("enter your last name")
# print(c)
# indexing starts from 0

print(len(mystr))
# print(mystr)
# print((mystr[0:6]))
# print(mystr[0:19])
# print(mystr[0:20])
# print(mystr[:])  # if not mentioned any size after collon it will take whole size by default
# print(mystr[0:423])  # any extra length will not give error
# print(mystr[:6])  # if not mentioned any staring range it will take 0 bydefalut
# print(mystr[:])  # it will take default values 0 and full length
# print(mystr[0::2])  # it will take every second word
# print(mystr[::3])  # first default values then every second word staring from index 0
# print(mystr[::1])  # first default values than every first word which is also default value for it
# print(mystr[::])  # all default values i.e 0,string length,1
# print(mystr[::3])  # every third word
# print(mystr[::32443])  # it will print only index 0 then nothing becoz length is not sufficent
# print(mystr[2:-1])  # negative indexing start reading from reverse staring from -1
# print(mystr[::-2])  # here it first start reading the str from reverse then every first word
# print(mystr[::-2])
# # Some function of string
# print(mystr.endswith("boy "))  # here it checks the last word and return a boolean value
# print(mystr.count("a"))  # here it counts the passed argument and returns int value
# print(mystr.capitalize())  # here it creates a new string with its first letter capitalized
# print(mystr.find("good"))  # here it returns the staring index of the found argument
# print(mystr.upper())  # here it creates a new string with all upper case letter
# print(mystr.lower())  # here it creates a new string with all upper case letter
# print(mystr.replace("is", "are"))
# print(mystr.swapcase())
b = "ararau"
a = mystr._add_(" "+b)
print(a)