# Banking program

def show_balance(balance):
    print("*****************")
    print(f"Your balance is: ${balance:.2f}")
    print("*****************")
    print()

def deposit():
    print("*****************")
    amount = float(input("Enter an amount to deposit: "))
    print("*****************")

    if amount < 0:
        print("*****************")
        print(T"hat is not a valid amount.")
        print("*****************")
        return 0

    else:
        return amount

def withdraw(balance):
    print("*****************")
    amount = float(input("Enter an amount to withdraw: "))
    print("*****************")

    if amount > balance:
        print("*****************")
        print("Insufficient funds.")
        print("*****************")

    elif amount < 0:
        print("*****************")
        print("Amount must be greater than 0.")
        print("*****************")

    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("*****************")
        print("Banking program")
        print("*****************")
        print()
        print("1. Show balance")
        print("2. Make a deposit")
        print("3. Withdraw money")
        print("4. Exit")

        print()
        print("*****************")
        choice = input("Please enter a number from 1-4: ")
        print("*****************")

        if choice == '1':
            balance == show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)
        
        elif choice == '4':
            is_running == False
            
        else:
            print("*****************")
            print("That is not a valid choice.")
            print("*****************")

print("Goodbye!")
StopIteration


if __name__ == '__main__':
    main()


