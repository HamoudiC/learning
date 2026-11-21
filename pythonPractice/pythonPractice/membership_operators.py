# Membership operators = used to test wether a value or variable is found in a sequence
#                       (string, list, set, tuple, or dictionary)
# 1. in
# 2. not in

word = "habood"

#letter guesser
while True:

    letter = input("Guess a letter in the secret word: ")

    if letter in word:
        print(f"The letter '{letter}' is in the secret word")
        break

    else:
        print(f"The letter '{letter}' is NOT in the secret word")
        break

#student finder
students = {"habood","mahdi","isabella"}

while True:

    student = input("Enter the name of a student: ")

    if student in students:
        print(f"{student} is a student")
        break

    else:
        print(f"{student} was not found")
        break


#dictionary
grade = {"sandy":"A", 
         "squidward":"B", 
         "spongebob": "C", 
         "patrick":"D"}

while True:
    person = input("Please enter the name of the student: ")

    if person in grade:
        print(f"{person}'s grade is: {grade}")
        break

    else:
        print(f"{person} was not found")
        break


email = "hamoudi0716@gmail.com"

if "@" in email and "." in email:
    print("Valid Email")
    

else:
    print("Invalid Email")



