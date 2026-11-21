# python writing files (.txt, .json, .csv)

#txt = Text

import os
 
txt_data = "Hello This is Bob. I am hiding somewhere."

file_path = "file_handling/writing_files/input.txt"


with open(file_path, "w") as file:
    file.write(txt_data)
    print(f"txt file '{file_path}' was created")

