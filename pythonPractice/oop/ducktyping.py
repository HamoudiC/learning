# "Duck Typing" = Another way to achieve polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True


class Dog(Animal):
    def speak(self):
        print("WOOF")


class Cat(Animal):
    def speak(self):
        print("MEOW")

#as long as this class has the same attributes as the others it will work as the others. 
class Car:

    alive  = False  #this alive attribute is not the same as the Animal attribute but it works because they have the same name
    def speak(self):  #this speak is not the same as the Animal speak but it works because they have the same name
        print("HONK")

animals = [Dog(),Cat(),Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)     
