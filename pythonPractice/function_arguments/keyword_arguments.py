# Function = A block of reusable code place () after the function name to invoke it

# Keyword argument: An argument preceded by an identifier
#                  Helps with readability
#                  Order of arguments doesn't matter

# Argument: 1. Positional  2. Default  3. KEYWORD  4. Arbitrary

def  hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title}.{first_name} {last_name}")

#Position wont matter since they are linked to each parameter.
#Positional arguments cant go in front of keyword arguments
hello("Hello",first_name= "Spongebob", last_name='Squarepants', title ="Mr.")


#print 1-10. End is a keyword argument. 
for x in range (1,11):
    print(x, end =" ")

#print 1-5 as strings and separates then with a "-". Sep is a keyword argument. (Separate)
print("1","2","3","4","5", sep="-")

