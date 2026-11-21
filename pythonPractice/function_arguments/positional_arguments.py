# Function = A block of reusable code place () after the function name to invoke it

# Positional argument: Values that are passed into a function based on their order. (a,b)

# Argument: 1. POSITIONAL  2. Default  3. Keyword  4. Arbitrary

#Function
def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} years old!")
    print(f"Happy birthday to {name}!")
    print()

#Positional Argument: Order matters (name,age)
happy_birthday("Habood", 20)

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of %{amount} is due on {due_date}")

display_invoice("habood", 12, "01/01")