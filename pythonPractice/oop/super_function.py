# super() = Function used in a child class to call methods from a parent class (Superclass).
#           Allows you to extend the functionality of the inherited methods

#superclass
class Shape:

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    
    def __init__(self, color, is_filled, radius):
        super(). __init__(color, is_filled)
        self.radius = radius

    #this overrides the parents "describe" method
    def describe(self):
        print(f"It is a circle with the area of {3.14 * self.radius * self.radius}cm^2")
        #use super() to use both versions of "describe"
        super().describe()

class Square(Shape):

    def __init__(self, color, is_filled, width):
        super(). __init__(color, is_filled)
        self.width = width

    #this overrides the parents "describe" method
    def describe(self):
        print(f"It is a square with the area of {self.width * self.width}cm^2")
        #use super() to use both versions of "describe"
        super().describe()

class Triangle(Shape):

    def __init__(self, color, is_filled, width, height):
        super(). __init__(color, is_filled)
        self.width = width
        self.height = height

     #this overrides the parents "describe" method
    def describe(self):
        print(f"It is a triangle with the area of {self.width * self.height / 2}cm^2")
        #use super() to use both versions of "describe"
        super().describe()

#keywords makes things more readable but not necessary 
circle = Circle("Red", True, 5)
square = Square(color = "Blue", is_filled = False, width = 6)
triangle = Triangle(color = "yellow", is_filled = True, height = 5, width = 6)


print(circle.color)
print(circle.is_filled)
print(f"{circle.radius}cm")
print()
print(square.color)
print(square.is_filled)
print(f"{square.width}cm")
print()
print(triangle.color)
print(triangle.is_filled)
print(f"{triangle.width}cm")

circle.describe()
square.describe()
triangle.describe()