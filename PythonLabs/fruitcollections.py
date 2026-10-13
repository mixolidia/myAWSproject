# Lab 4: Working with Lists, Tuples, and Dictionaries
#ex.1
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

print(myFruitList[0])
print(myFruitList[1])
print(myFruitList[2])

myFruitList[2] = "orange"

print(myFruitList)

#ex.2   
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

#ex.3
myFavoriteFruitDictionary = {"Akua" : "apple", "Saanvi" : "banana", "Paulo":"pineapple"}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
first_key = list(myFavoriteFruitDictionary.keys())[0]
print(first_key)  # Output: Akua
print(list(myFavoriteFruitDictionary.keys())[0]) # Akua
print(myFavoriteFruitDictionary[first_key]) # apple
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])