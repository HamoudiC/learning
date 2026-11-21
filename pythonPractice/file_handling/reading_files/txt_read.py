# Python reading files (.txt, .json, .csv)


# get the file to read it
file_path = "file_handling/writing_files/input.txt"

try: 
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File has not yet been opened or does not exist.")

except PermissionError:
    print("You do not have permission to read this file.")
