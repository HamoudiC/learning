# collection = single "variable" used to store multiple values
#       List = [] ordered and changeable. Duplicates OK
#        Set = {} unordered and immutable, but Add/Remove OK. No duplicates allowed
#      Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = {"apple", "orange", "banana", "coconut"}

# len(): prints length of fruits
print(len(fruits))

#checks if an element is in the set
print("pineapple" in fruits)

# .remove(): removes an element from the set
fruits.remove("apple")

# .add(): adds an element to the set
fruits.add("apple")

# .pop(): removes the first element in the set. (random since sets are unordered)
fruits.pop()

print(fruits)

# use print(dir(fruits or wtv)) to see all methods available
# use print(help(fruits or wtv)) to see all descriptions of the methods from dir()

