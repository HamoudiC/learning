# Polymorphism = Greek word that means "To have many forms or faces"

#         Poly = Many
#       Morphe = Form

from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2      # ** means to the power of

class Square(Shape):
    
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
        
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    

#multi-level inheritance. Inherits area function: Shape -> Circle -> Pizza
class Pizza(Circle):                        
    def __init__(self,topping, radius):
        self.topping = radius
        self.radius = radius

shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("Pepperoni", 12)]

for shape in shapes:
    print(f"{shape.area()}cm^2")

