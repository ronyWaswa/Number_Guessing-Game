import random


def play():
    secret = random.randint(1, 100)
    max_tries = 7
    tries = 0

    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_tries} tries.")

    while tries < max_tries:
        try:
            guess = int(input(f"\nGuess #{tries + 1}: "))
        except ValueError:
            print("Please enter a whole number.")
            continue  # invalid input does not use up a try

        tries += 1

        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Correct! You got it in {tries} tries.")
            return

    print(f"\nGame over. The number was {secret}.")


while True:
    play()
    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing!")
        break