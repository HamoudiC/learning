# concession stand program

menu = {"pizza":3.00,
        "nachos":2.50,
        "hotdog":2.25,
        "burger":5.00,
        "fries":1.75,
        "pretzel": 2.00,
        "water bottle":0.10,
        "lemonade":0.75}

#empty list
cart = []

total = 0

print("------MENU------")
for key, value in menu.items():
    print(f"{key:10} ${value:.2f}")

print("----------------")

while True:

    #gets food item from input
    food = input("Select an item to buy. ('q' to quit) ").lower()

    if food == "q":
        break

    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end="  ")

print()
print("-------YOUR ORDER-------")
print()
print(f"Total is: ${total:.2f}")

