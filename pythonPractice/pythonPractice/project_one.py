# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter username: ")

if len(username) > 12:
    print("Your username is too long.")

elif not username.find(" ") == -1:
    print("Username can't contain spaces.")

elif not username.isalpha():
    print("Username can't contain numbers")

else:
    print(f"welcome {username}")

