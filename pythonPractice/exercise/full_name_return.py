# functions = A block of reusable code
#             place () after the function name to invoke it

def create_name(first_name, last_name):

    first = first_name.capitalize()
    last = last_name.capitalize()

    full_name = first +" "+last
    return full_name


print(create_name("Habood","Cheaito"))

# .capitalize(): capitalized first letter in a string