# Python writing files (.txt, .json, .csv)

#modes
# "w" = writes if file exists, if it doesn't, we receive an error 
# "x" = writes if file doesn't exist, if it does we will receive an error
# "a" = append
# "r" = read


# w mode
txt_data = "I like Pizza"

file_path = "file_handling/modes/test.txt"

with open(file_path, "w") as file:      
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

# this is generally the most used mode