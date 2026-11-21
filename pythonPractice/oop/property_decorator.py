# @property = Property Decorator is used to define a method as a property
#             It can be accessed as an attribute
#             Benefit: Add additional logic when read, write or delete attribute
#             Gives you getter, setter and setter method

class Rectangle:

    def __init__(self, width, height):

        self._width = width           #adding the _ in _width means that its supposed to be private functions.
        self._height = height         # same here

    #getter methods
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(self, new_width):

        if new_width > 0:
            self._width = new_width

        else:
            print("Width must be above 0")

    @height.setter
    def height(self, new_height):

        if new_height > 0:
            self._width = new_height

        else:
            print("Height must be above 0")

    def area(self):
        area  = self.new_height * self.new_width
        return f"Area of Rectangle: {area:.1f}cm^2"
    
    @width.deleter

    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
    

rectangle = Rectangle(12,10)
rectangle.width = 5
rectangle.height = 9


#deleter
del rectangle.width
del rectangle.height


print(rectangle.width)
print(rectangle.height)
rectangle.area()



#find issue later and fix it