#os module
import os

#prints all attributes and methods in the os module
print()
print("ALL ATTRIBUTES AND METHODS IN os MODULE:")
print(dir(os))

#prints current directory
print()
print(os.getcwd())

#how to change directory
print()
print("CURRENT DIRECTORY")
os.chdir('C:/Users/hamou/Downloads')
print(os.getcwd())

#How to see the files and folders from the specified directory
print()
print("EVERYTHING ON CURRENT DIRECTORY")
print(os.listdir())

#How to create a new folder on current directory
print()
print("HOW TO CREATE A FOLDER IN CURRENT DIRECTORY:")
try:
    folder = os.makedirs('os_module-2/Sub-Dir-1')    
    print(f"{folder} Created")

except FileExistsError:
    print("This file already exists.") 


#How to delete folders in current directory
print()
print("HOW TO DELETE FOLDERS IN CURRENT DIRECTORY:")

# HOW TO DELETE FILES

#os.remove('single_file.txt')  # Deletes a single file

# HOW TO DELETE FOLDERS

# Option 1: Delete an empty folder
#os.rmdir('empty_folder')  # Only works if folder is empty

# Option 2: Delete a folder with stuff inside
folder = os.rmdir('os_module-2/Sub-Dir-1')  # Deletes folder and everything in it
print(f"{folder} was Deleted.")

# Rename file or folder ('original name','new name')
print()
print("HOW TO RENAME FILE OR FOLDER:")
try:
    name = os.makedirs("test.txt")
    rename = os.rename('test.txt','demo.txt')
    print(f"Renamed: {name} to {rename}")

except FileExistsError:
    print(f"File already exists")
    user_input = input("Would you like to delete the file? (Y/N) ").upper()

    if user_input == 'Y':
        rename = os.rmdir('demo.txt')
        print("File has been deleted.")
    
    else:
        print("File still exists")

# How to get info on file
print()
print("HOW TO GET INFO FROM A SPECIFIC FILE:")
print(os.stat("demo.txt"))

# How to view entire directory tree
print()
print("HOW TO VIEW ENTIRE DIRECTORY TREE")

for dirpath, dirname, filenames in os.walk('C:/Users/hamou/Downloads'):
    print("Current Path:", dirpath)
    print("Directories: ", dirname)
    print("Files: ", filenames)
    print()

# How to access home directory
print()
print("HOW TO ACCESS HOME DIRECTORY:")


file_path = print(os.environ.get('HOME')) + 'text.txt'


