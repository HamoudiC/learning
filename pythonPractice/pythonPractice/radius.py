import math


#radius for circle
radius = float(input("Please enter the radius of a circle: "))

circumference = 2 * math.pi * radius
area = math.pi * pow(radius,2)

# 2 is for 2 decimal spaces
print(f"The area of the circle is: {round(area,2)}cm^2")

print(f"The circumference is: {round(circumference,2)}cm")

