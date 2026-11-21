# collection = single "variable" used to store multiple values
#       List = [] ordered and changeable. Duplicates OK
#        Set = {} unordered and immutable, but Add/Remove OK. No duplicates allowed
#      Tuple = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ("apple", "orange", "banana", "coconut")

# .len(): prints length of tuple
print(len(fruits))

#.index("element"): prints the index of the specific element
print(fruits.index("apple"))

# .count("element"): prints the amount of a specific element in a tuple
print(fruits.count("apple"))


# use print(dir(fruits or wtv)) to see all methods available
# use print(help(fruits or wtv)) to see all descriptions of the methods from dir()


#Use a tuple instead of a list when possible