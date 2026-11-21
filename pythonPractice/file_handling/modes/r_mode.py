# Python writing files (.txt, .json, .csv)

#modes
# "w" = writes if file exists, if it doesn't, we receive an error 
# "x" = writes if file doesn't exist, if it does we will receive an error
# "a" = append
# "r" = read

#get the file written from the "w" mode
file_path = "file_handling/modes/test.txt"

try:
    with open(file_path, "r") as file:

        #make a variable so you can print the data inside the file
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File has not yet been opened or does not exist.")
