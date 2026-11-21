# python writing files (.txt, .json, .csv)

#CSV = Comma Separated Values

import csv
 
input = [["Name","Age","Job"],
            ["Spongebob",30,"Cook"],
            ["Patrick",35,"Janitor"],
            ["Squidward",36,"Cashier"]]

file_path = "file_handling/writing_files/input.csv"

try:
    with open(file_path, "w", newline = "") as file:
        writer = csv.writer(file)
        for row in input:
            writer.writerow(row)
        print(f"CSV file '{file_path}' was created")

except FileExistsError:
    print("That file already exists!")