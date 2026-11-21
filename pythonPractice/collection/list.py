# collection = single "variable" used to store multiple values
#       List = [] ordered and changeable. Duplicates OK
#        Set = {} unordered and immutable, but Add/Remove OK. No duplicates allowed
#      Tuple = () ordered and unchangeable. Duplicates OK. FASTER

#List
fruits = ["apple","banana","pineapple","mango"]
print(fruits[::-1])

#check if an element is in list (boolean): "value" in list. 
print("apple" in fruits)

#.remove(): removes an element
fruits.remove("pineapple")

#.append(): adds element to the end of the list
fruits.append("guava")

#reassign element: overrides the element at that position
fruits[0] = "orange"

#.insert(position, "name"): adds an element at specified position. Pushes the element at that position back 1.
fruits.insert(2,"raspberries")
print(fruits)

#.sort(): sorts by alphabetical order
fruits.sort()

#.reverse(): reverses the list. To reverse alphabetical order do .sort() then .reverse()
fruits.reverse()

#.clear(): clears the entire list
#fruits.clear()

#.index("element"): returns the index of the element
fruits.index("guava")

#.count("element"): counts how many of one element are in the list
fruits.count("apple")

#print length of fruits list
print(len(fruits))

#print every fruit in fruits for loop
for fruit in fruits:
    print(fruit)

# use print(dir(fruits or wtv)) to see all methods available
# use print(help(fruits or wtv)) to see all descriptions of the methods from dir()




