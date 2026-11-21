# #Function = A block of reusable code place () after the function name to invoke it

# Arbitrary arguments: = Lets a function accept ANY number of arguments instead of a fixed amount
# *args    = allows you to pass multiple non-key arguments  (agrs = arguments)         
# **kwargs = allows you to pass multiple keyword- arguments (kwargs = keyword arguments)
# *        = unpacking operator                  
# Argument:           1. Positional  2. Default  3. Keyword  4. ARBITRARY

#adds up all the values that are passed through the function
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1,2,3,4,5,6,7,8,9))

#passes all values into the function. Position matters since there is no keywords to define the words.
def display_name(*args):
    for key in args:
        print(key, end=" ")

print("Dr.", "Spongebob", "Squarepants", "IV")


def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
#                 ^        ^
#                key      value
print_address(Number = "79", 
              Street = "Laurier",
              Road_Type = "Avenue",
              City = "Richmond Hill",
              Province = "ON")

#*agrs should always be before **kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(f"{arg}", end= " ")


    if "apt" in kwargs:
        print({kwargs.get('apt')})
    print(f"lives at: {kwargs.get('number')} {kwargs.get('street')} {kwargs.get('city')}, {kwargs.get('postal_code')}")


#same here
shipping_label("Dr.","Spongebob","Squarepants","IV",
               street = "Laurier",
               number = "79",
               city = "Richmond Hill",
               postal_code = "L4E 4P5")

