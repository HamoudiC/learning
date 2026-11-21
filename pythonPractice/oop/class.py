# class variables = Shared among all instances of the class
#                   Defined outside the constructor
#                   Allow you to share data among all objects created from that class

class student:

    #class variable
    class_year = 2026
    num_students = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.num_students += 1

student1 = student("Spongebob", 30)
student2 = student("Patrick", 35)
student3 = student("Squidward", 39)
student4 = student("Sandy", 27)

#class variable is local so all instances from the class shares it.
# access the class variable from the class name (better and clearer)

print(student.class_year)
print(f"My graduating class of {student.class_year} has {student.num_students} students: ")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)