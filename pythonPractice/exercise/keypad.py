# 2D keypad (2D tuple)

#Set: NO (because it is unordered and numbers will go in random positions every time I run the code)
#List: OK (List is fine because it is ordered)
#Tuple: BEST (Faster than list)

num_pad = ((1, 2, 3),
           (4, 5, 6,),
           (7, 8, 9,),
           ("*", 0, "#"))

for row in num_pad:
    for digit in row:
        print(digit, end=" ")
    print()