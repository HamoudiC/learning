#hangman python
import random 

words = (
    "apple", "banana", "orange", "grape", "peach", "cherry", "melon", "lemon",
    "computer", "keyboard", "mouse", "screen", "python", "coding", "program",
    "variable", "function", "loop", "string", "integer", "asteroid", "eraser",
    "school", "teacher", "student", "homework", "notebook", "pencil", "lightning" 
    "library", "science", "history", "weather", "storm", "thunder", "battle", 
    "game", "player", "score", "level", "enemy", "weapon", "armor", "melody",
    "victory", "defeat","music", "guitar", "piano", "drums", "violin", 
    "movie", "actor", "director", "camera", "scene", "script", "desert",
    "animal", "tiger", "lion", "elephant", "giraffe", "zebra", "monkey",
    "dog", "cat", "rabbit", "hamster", "rhythm", "rainbow", "snowflake", 
    "space", "planet", "galaxy", "rocket", "astronaut", "comet", 
    "ocean", "island", "beach", "mountain", "forest"  
)

#dictionary of key:()
hangman_art = {0:("   ",
                  "   ",
                  "   "),

               1:(" o ",
                  "   ",
                  "   "),

               2:(" o ",
                  " | ",
                  "   "),

               3:(" o ",
                  "/| ",
                  "   "),

               4:(" o ",
                  "/|\\ ",
                  "   "),

               5:(" o ",
                  "/|\\ ",
                  "/  "),

               6:(" o ",
                  "/|\\ ",
                  "/ \\ ")}


def display_man(wrong_guess):
    for line in hangman_art[wrong_guess]:
        print(line)
        


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        display_man(wrong_guesses)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid Input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed.")
            continue

        guessed_letters.add(guess)

        if guess in answer: 
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] == guess



if __name__ == "__main__":
    main()
