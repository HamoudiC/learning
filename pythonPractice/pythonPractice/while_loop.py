# while loop = execute some code WHILE a condition remains true

name = input("Please enter name: ")

while name == "":
    print("Name cannot be empty")
    name = input("Please enter your name: ")

print(f"Hello {name}")



age = int(input("Enter your age: "))

while age <= 0:
    print("Age must be over 0")
    age = int(input("Enter your age: "))

print(f"You are {age} years old.")   


food = input("Enter a food you like: ")

while not food == 'q' :  
    print(f"You like {food}. To quit please enter 'q'")
    food = input("Enter a food you like: ")

print("Bye")





