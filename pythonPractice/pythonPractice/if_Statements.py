# If = Do some code only IF some condition is TRUE
# Else = ELSE do some code  if condition is FALSE

#condition
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")

elif age >= 18:
    print("You are now signed up!")

elif 0 >= age:
    print("You have not been born yet.")

else:
    print("You must be 18+ to sign up.")

#boolean

online = False #False ignores if statement, True ignores else statement.

if online:
    print("You are online")

else:
    print("You are offline")