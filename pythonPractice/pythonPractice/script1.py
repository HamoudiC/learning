# Functions and classes in this module can be reused without the main block of code executing
# Code is modular, helps readability, leaves no global variables, avoids unintended execution


def favorite_food(food):
    print(f"Your favorite food is: {food}")
    

def main():
    print("This is script 1")
    favorite_food("pizza")
    print("Goodbye!")

if __name__ == '__main__':
    main()
