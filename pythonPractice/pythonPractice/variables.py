# variables  = A container for a value (string, integer, float, boolean)
#              A  variable behaves as if it was the value it contains.


#Strings
first_name = "habood"
food = "pizza"
email = "haboudi0716@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food} {first_name} your email is: {email}")


#Int
age = 25
quantity = 3;
num_of_students = 30

print(f"You are {age} years old.")
print(f"You are {age} buying {quantity} games bro. Let us {num_of_students} students get some man.")

#Float
price = 10.99
gpa = 4.9
distance = 5.5


print(f"Damn u got no life. Your GPA is {gpa}...")
print(f"You ran {distance}km tdy. Nice!")

#Boolean

is_Student = True
for_Sale = False
is_Online = True

print(f"You are a student: {is_Student}")

if is_Student:
    print("You are a Student")

else: 
    print("You are NOT a Student")

if for_Sale:
    print("Item is for sale.")

else:
    print("Item is NOT for sale")

if is_Online:
    print("You are online")
    
else:
    print("You are NOT online")




