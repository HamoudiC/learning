# Static Method = A method that belongs to a class rather than any object from that class (instance)
#                 Usually used for general utility functions

# Instance Method = Best for operations on instances of the class (objects)
# Static Methods = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self,name,position):
        self.name = name 
        self.position = position

    #Instance Method
    def get_info(self):
        return f"{self.name} = {self.position}"
    
    #Static Method 
    @staticmethod
    def is_valid_position(position):
        valid_position = ["Manager","Cashier","Cook","Janitor"]
        return position in valid_position
    
employee1 = Employee("Eugene", "Manager")
employee2 = Employee("Squidward", "Cashier")
employee3 = Employee("Spongebob", "Cook")
employee4 = Employee("Patrick", "Janitor")

  
print(Employee.is_valid_position("Cashier"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())
print(employee4.get_info())
    


    

    
