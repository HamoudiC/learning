# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

#dog now has all the attributes from the animal class
class Dog(Animal):
    
    def speak(self):
        print("WOOF")

class Cat(Animal):
    
    def speak(self):
        print("MEOW")

    def snack(self):
        print(f"{cat.name} is eating {mouse.name}")


class Mouse(Animal):
    
    def speak(self):
        print("SQUEAK")

dog = Dog("Scooby")
cat = Cat("Garfeild")
mouse = Mouse("Mickey")

#has all the functions from the Animal class
print(dog.name)
print(cat.name)
print(mouse.name)

#functions from each class
cat.snack()
mouse.speak()