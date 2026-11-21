# multiple inheritance = inherit from more than one parent class
#                        class you(mom,dad)
#                        mom + dad = you

#  multilevel inheritance = inherit from a parent which inherits from another parent
#                           class parent(grandparent) 
#                           class you(parent)
#                           grandpa -> dad -> you

#grandparent class
class Animal:

    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


#parent classes, take the eat and sleep functions from the Animal class (grandparent)
class Prey(Animal):

    def flee(self):
        print(f"{self.name} is hunting")

class Predator(Animal):

    def hunt(self):
        print(f"{self.name} is fleeing")


#child classes
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

#multiple inheritance, took both the prey class and predator class
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Peter")
hawk = Hawk("Hawk Tuah")
fish = Fish("Bob")

#rabbit can only flee
print(rabbit.flee())

#hawk can only hunt
hawk.hunt()

#fish can do both
fish.flee()
fish.hunt()

# multi-level inheritance, rabbit, hawk and fish got the animal class functions 
# through the prey and predator classes
rabbit.eat()
rabbit.sleep()

hawk.eat()
hawk.sleep()

fish.eat()
fish.sleep()

