# #Function = A block of reusable code place () after the function name to invoke it

# Default arguments = A default value for certain parameters.
#                     Default is used when that argument is omitted.
#                     Makes functions more flexible and reduces # of arguments

# Argument:           1. Positional  2. DEFAULT  3. Keyword  4. Arbitrary

# discount and tax now have a default argument. They are Fallback values
def net_price(original_price, discount = 0, tax = 0.13):

    return original_price * (1 - discount) * (1 + tax)

# if we add a discount value or tax value it overrides the default argument.
print(net_price(500))

