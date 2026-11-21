# Python File Detection 

import os       # os = operating system

file_path = "file_handling/test.txt"

if os.path.exists(file_path):
    print(f"The location '{file_path}' exists")

    if os.path.isfile(file_path):
        print("That is a file.")
    
    elif os.path.isdir(file_path):
        print("This is a directory")

else:
    print("That location does not exist")
