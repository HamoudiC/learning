# List comprehension = A concise way to create lists in python
#                      Compact and easier to read than traditional loops
#                      ['expression' for 'value' in 'iterable' if 'condition']

doubles = []

#original boring for loop
for x in range (1,11):
    doubles.append(x * 2)

print(f"BORING: {doubles}")

#newer and cooler for loop
doubles = [x * 2 for x in range(1,11)]
print(f"COOL: {doubles}")

#Examples
triples = [y * 3 for y in range(1,11)]
print(triples)

squares = [z * z for z in range(1,11)]
print(squares)

#Prints first letter of every value
fruits = ["Apple","Orange","Banana","Mango"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)