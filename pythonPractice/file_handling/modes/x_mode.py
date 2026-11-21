# Python writing files (.txt, .json, .csv)

#modes
# "w" = writes if file exists, if it doesn't, we receive an error 
# "x" = writes if file doesn't exist, if it does we will receive an error
# "a" = append
# "r" = read


# x mode
txt_data = "How did you find this file man. -bob"

file_path = "file_handling/modes/test_bob.txt"

try:
    with open(file_path, "x") as file:      
        file.write(txt_data)
        print(f"txt file '{file_path}' was created")

except FileExistsError:
    print("That file already exists")

# Creates the file and adds text and stuff inside it. Wont create if it already exists and will give an error message.