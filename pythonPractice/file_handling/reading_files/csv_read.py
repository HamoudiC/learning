# Python reading files (.txt, .json, .csv)

import csv

# get the file to read it
file_path = "file_handling/writing_files/input.csv"

try: 
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])              #can also access column: print(line[0]) or [1], [2], [3]

except FileNotFoundError:
    print("File has not yet been opened or does not exist.")

except PermissionError:
    print("You do not have permission to read this file.")