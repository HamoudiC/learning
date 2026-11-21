# Conditional Expression = A one-line shortcut for the if-else statement (ternary operator)
#                          Print or assign one of two values based on a condition
#                Formula = 'X' if 'condition', else 'Y'

num = 5
a = 6
b = 7

#         X          condition       Y
print("Positive" if num > 0 else "Negative")

max_num = a if a > b  else b
print(max_num)

min_num = a if a < b else b
print(min_num)

age  = 12
status = "Adult" if age >= 18 else "Child"
print(status)


temp = 21
weather = "HOT" if temp > 20 else "COLD"
print(weather)

user_role = "guest"
access_level = "Full Access" if user_role == "admin" else "Limited Access"
print(access_level)