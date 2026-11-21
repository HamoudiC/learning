# Python reading files (.txt, .json, .csv)

import json

# get the file to read it
file_path = "file_handling/writing_files/input.json"

try: 
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)              #can also access key: print(content["name"]) or "age" or "job"

except FileNotFoundError:
    print("File has not yet been opened or does not exist.")

except PermissionError:
    print("You do not have permission to read this file.")