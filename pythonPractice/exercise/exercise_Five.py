#shopping cart program (using collections)

foods = []
prices = []
total = 0

while True:
    food = str(input("Please enter food you want to buy (press 'q' to quit): "))
    
    if food.lower() == 'q':
        for price in prices:
            total += price
        print()
        print(f"Your total is: ${total}")
        break

    else:
        price = float(input("Enter the price of the food item: $"))
        foods.append(food)
        prices.append(price)
        
print()
print("-----YOUR CART-----")

for food in foods:
    print(f"• {food}")

      
