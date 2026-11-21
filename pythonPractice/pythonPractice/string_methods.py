#String Methods

name = input("Enter your full name: ")

# len() returns the length of string (counts spaces and all characters)
length = len(name)
print(length)

# find() returns the position of the first match of the specified character
first_space = name.find(" ")
print(first_space)

# rfind() returns the position of the LAST match of the specified character
last_space = name.rfind(" ")
print(last_space)

# capitalize() capitalizes the first letter of the string, rest lowercase
cap = name.capitalize()
print(cap)

# upper() converts ALL letters to uppercase
upper = name.upper()
print(upper)

# lower() converts ALL letters to lowercase
lower = name.lower()
print(lower)

# isdigit() returns True if string contains ONLY digits (no spaces/letters)
digit = name.isdigit()
print(digit)

# isalpha() returns True if string contains ONLY letters (no spaces/digits)
alpha = name.isalpha()
print(alpha)

# replace(old, new) replaces all occurrences of old substring with new substring
# Example: replace(" ", "-") would replace spaces with dashes
replace = name.replace(" ", "") 
print(replace)

# count() returns how many times a character/substring appears in the string
count = name.count('o')
print(count)


#example
phone_number = input("Input your phone number: ")
val = input("input value you want to count: ")
counter = phone_number.count(val)
print(f"You have {counter} '{val}' in your phone number.")


#to see all string functions do print(help(str))
