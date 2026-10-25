import random


def guessNumber():
    numberToGuess = random.randint(1, 100)
    difficulties = {
        "1": ("Easy", 10),
        "2": ("Medium", 5),
        "3": ("Hard", 3),
        "easy": ("Easy", 10),
        "medium": ("Medium", 5),
        "hard": ("Hard", 3),
    }

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Guess the number before you run out of chances.")
    print("Please select a difficulty level:")
    print("1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)")

    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice in difficulties:
            difficultyName, attemptsLeft = difficulties[choice]
            break
        print("Invalid choice. Please select easy, medium, or hard (1, 2, or 3).")

    print(
        f"Great! You have selected the {difficultyName} difficulty level."
        "\nLet's start the game."
    )
    print(f"You have {attemptsLeft} chances to guess the correct number.")

    attempts = 0
    while attemptsLeft > 0:
        try:
            userGuess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a whole number between 1 and 100.")
            continue

        if not 1 <= userGuess <= 100:
            print("Please enter a number between 1 and 100.")
            continue

        attempts += 1
        attemptsLeft -= 1
        if userGuess == numberToGuess:
            print(
                f"Congratulations! You guessed the correct number in "
                f"{attempts} attempts."
            )
            return
        if userGuess > numberToGuess:
            print(f"Incorrect! The number is less than {userGuess}.")
        else:
            print(f"Incorrect! The number is greater than {userGuess}.")

    print(f"Game over! The number was {numberToGuess}.")


if __name__ == "__main__":
    guessNumber()
