# input() = A function that prompts the user to enter data 
#           Returns the entered data as a string


#birthday function
name = input("What is ur name?: ")
age = input("How old are you?:")

age = int(age)
age = age + 1

print(f"Hello {name}!")
print("Happy birthday!")
print(f"You are {age} years old!")

if age == 18:
    print("You are now an adult!")
