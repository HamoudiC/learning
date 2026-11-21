# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          You need a "class" to create many objects

# class =  (blueprint) used to deign the structure and layout of an object

class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale


    def stop(self):
        print(f"You are the {self.color} {self.model}.")


    def drive(self):
        print(f"You stopped the {self.color} {self.model}.")

    def describe(self):
        print(f" {self.year} {self.color} {self.model}")