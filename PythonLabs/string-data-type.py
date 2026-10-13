# Working with the String Data Type
# ex.1
myString = "This is a string"
print(myString)

print(type(myString))

print(myString + " is of the data type " + str(type(myString))) 
print(myString + " is of the data " +type(myString).__name__)

#ex.2
firstString = "water"

secondString = "fall"

thirdString = firstString + secondString

print(thirdString)

#ex.3
name = input("What is your name? ")
print(name)

#ex.4
color = input("What is your favorite color?  ")

animal = input("What is your favorite animal?  ")

print("{}, you like a {} {}!".format(name,color,animal))