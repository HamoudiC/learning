# python writing files (.txt, .json, .csv)

#JSON =  JavaScript Object Notation

import json

#JSON: must have key:value pairs

input = {
            "name":"Spongebob",
            "age": 30,
            "job":"cook"
             }

file_path = "file_handling/writing_files/input.json"      

try:
    with open(file_path, "w") as file:
            json.dump(input, file, indent=4)
            print(f"json file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")

except TypeError:
    print("Object must be a string not a list.")







