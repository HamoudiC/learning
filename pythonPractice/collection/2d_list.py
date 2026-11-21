#2D list

fruits = ["apple", "orange", "banana", "coconut"]       #fruits becomes index 0 in groceries
vegetables = ["carrot", "lettuce", "potatoes"]          #vegetables becomes index 1 in groceries
meats = ["turkey", "fish", "chicken"]                   #meats becomes index 2 in groceries

groceries = [fruits, vegetables, meats]

print(groceries[1][2])

#Or different format

cars = [["M2","M3","M4",]
        ["RS3","RS$","RS5"]
        ["C43","C63", "C63s"]]

#to iterate through all elements in cars do this: 
for car in cars:
    print(cars)

#to iterate over every element in every row in cars do this:
for car in cars:
    for model in cars:
        print(model, end=" ")           #end=" ": the spaces makes all elements 
        print()                         #have a space in between instead of each one on a new line


