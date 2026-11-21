# Decorator = A function that extends the behavior of another function
#             without modifying the base function
#             Pass the base function as an argument to the decorator

#decorator
def add_sprinkles(func):
    
    #INNER function
    def wrapper(*args, **kwargs):
        print("You added sprinkles! 🎊")
        func(*args, **kwargs)
    return wrapper

# another decorator
def add_fudge(func):
    
    #INNER function
    def wrapper(*args, **kwargs):
        print("You added fudge! 🍫")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):

    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("Strawberry")






#Formula for decorator functions: 

#decorator function
#def name_of_function(func):
    
    #INNER function
#    def wrapper():
#        func()
#    return wrapper