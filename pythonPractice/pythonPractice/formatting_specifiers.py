# format specifiers = {value:flags} format a value based on what flags are inserted

#flags:

# .{number}f = round to that many decimal spaces (fixed point)
# :{number} = allocate to that many spaces
# :03 = allocate and zero pad to that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive integers
# :, = comma separator 

price1 = 3000
price2 = -987.65
price3 = 12.34

#                    value : flag
print(f"price 1 is: ${price1:,}")
print(f"price 2 is: ${price2:^5}")
print(f"price 3 is: ${price3:>10}")





