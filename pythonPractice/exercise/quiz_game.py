#quiz game

#tuple
questions = ( "How many planets are in our solar system: ",
              "What is 1+1?: ",
              "What is the best car brand in the world?: ",
              "What is the worst car brand in the world: ",
              "Audi vs BMW: who wins?: ")

#tuple
options = (("A. 12", "B. 2", "C. 9", "D. 8"),
           ("A. 15", "B. 231", "C. 2", "D. 4"),
           ("A. BMW", "B. Mercedes", "C. Toyota", "D. Audi"),
           ("A. BMW", "B. Mercedes", "C. Toyota", "D. Audi"),
           ("A. Audi", "B. BMW"))

#tuple
answers = ("D","C","A","D","B")

#list
guesses = []

question_num = 0
score = 0

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
            print(option)

    question_num += 1

    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)

    if guess == answers:
        print("Correct")
        score += 1

    else:
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")

        if score == 0:
            score -= 0

        else:
            score -= 1

    if score >= 3:
        print("-------------------")
        print("      RESULTS      ")
        print("-------------------")
        print(f"Nice you passed! Score: {score}")
    
    elif score == 2:
        print("Guesses: ", end="")
        for guess in guesses:
            print(guess, end=" ") 
        print("-------------------")
        print("      RESULTS      ")
        print("-------------------")
        print(f"You alost passed! Try Again. Score: {score}")

    else:
        print("-------------------")
        print("      RESULTS      ")
        print("-------------------")
        print()
        print(f"U are a dumbass. Score: {score}")
