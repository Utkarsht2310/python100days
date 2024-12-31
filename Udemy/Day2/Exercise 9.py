
import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            guess = int(input("Make a guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low.")
            elif guess > number_to_guess:
                print("Too high.")
            else:
                print(f"You got it! The number was {number_to_guess}. You guessed it in {attempts} attempts.")
                guessed = True
        except ValueError:
            print("Please enter a valid number.")

number_guessing_game()
