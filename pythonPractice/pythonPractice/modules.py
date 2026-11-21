# module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program into reusable separate feels

#to see all modules do print(help("modules"))
# to see all the specific module do print(help(specific module)) 

#import
import math 
print(math.pi)

#change the name of the module if its too long:
import math as m
print(m.pi)

#importing a module from another file
#import file first
import module_example

result = module_example.pi
result = module_example.square(3)
result = module_example.cube(3)
result = module_example.circumference(3)


#print the any module from the file
print(result)