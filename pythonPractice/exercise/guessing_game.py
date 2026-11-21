import random

low = 1
high = 100

guesses = 0

number = random.randint(low,high)

while True:
    guess = int(input("Guess a number between 1-100 (type '404' to exit.): "))
    
    if guess == 404:
        print("Goodbye!")
        break

    elif guess == number:
        guesses += 1
        print(f"Congrats! It took you {guesses} tries to guess the correct number!")
        break

    elif number > guess :
        guesses += 1
        print("That number was too low!")

    elif guess > number:
        guesses += 1
        print("That number is too high!")
