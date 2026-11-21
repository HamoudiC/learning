# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"Canada":"Ontario",
            "USA": "Washington D.C",
            "China":"Beijing",
            "Russia": "Moscow"}

#gets dictionary
print(capitals.get("USA"))
print(capitals.get("Russia"))

if capitals.get("tokyo"):
    print("That capital exists")

else:
    print("That capital does not exist")

# .update({key:value}): updates list with new key and value 
capitals.update({"Germany":"Berlin"})
print(capitals)         #germany goes to the end of the list

#update new capital (or change a value or key)
capitals.update({"USA":"Detroit"})

#USA will now have Detroit instead of Washington D.C

# .pop("key"): removes the specified key (which removes the values as well)
capitals.pop("China")

# .popitem(): removes the newest key:value pair
capitals.popitem()

# .add("key";"value"): adds a key:value pair
capitals.add({"China":"Beijing"})

capitals.add({"":"beirut"})     #added value to empty key
capitals.add({"Lebanon":""})    #added key with empty value

# .clear(): clears entire dictionary
#capitals.clear()

# variable = dictionary.keys(): gets all the keys in dictionary {keys:""}
keys = capitals.keys()
print(keys)

#how to list all keys alone
for key in capitals:
    print(key)

# variable = dictionary.values(): gets all the values in the dictionary {"":values}
values = capitals.variables()
print(values)

#how to list all values alone
for value in capitals.values():
    print(value)

# variable = dictionary.item(): returns a dictionary OBJECT that resembles a 2D LIST of TUPLES
items = capitals.items()

#print every key and value in object
for key, value in capitals.item():
    print(f"{key}:{value}")



# use print(dir(capitals or wtv)) to see all methods available
# use print(help(capitals or wtv)) to see all descriptions of the methods from dir()