# Exercise 2: Shopping Cart Program

item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price * quantity

if quantity >= 2: 
    print(f"You have bought {quantity}x {item}'s")

else:
    print(f"You have bought {quantity}x {item}")
print(f"Your total is: ${total}")

