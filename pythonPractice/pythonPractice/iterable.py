# Iterable = An object/collection that can return its elements one at a time,
#           allowing it to be iterated over in a loop.

#lists are iterable
numbers = [1,2,3,4,5]

for number in numbers:
    print(number)

#reverse
for number in reversed(numbers):
    print(numbers, end=",")


#tuples are iterable
letters = ('a','b','c','d')

for letter in letters:
    print(letter, end=",")

#reverse
for letter in reversed(letters):
    print(letter, end=",")


#sets are iterable (not reversible though)
fruits = {"apple","banana","orange","strawberry"}

for fruit in fruits:
    print(fruit, end=",")

#Iterates the letters in the string
name = "Habood"

for letter in name:
    print(letter,end=" ")


#dictionaries
my_dictionary = {"A":1, "B":2, "C":3, "D":4}


#Prints the keys in my_dictionary. "Key":Value
for key in my_dictionary:
    print(key)

#Prints the value in my_dictionary. "Key":Value
for value in my_dictionary:
    print(value)

#Prints the items in my_dictionary. "Key":Value
for key,value in my_dictionary.items():
    print(f"{key}:{value}")
