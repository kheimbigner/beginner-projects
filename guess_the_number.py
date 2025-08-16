import tkinter as tk
import random as number

print("Welcome to the Guess the Number Game!")

# Initialize the guess counter
guess_count = 0

# Set the maximum number of guesses
max_guesses = 3

# Main game loop
def number_guess():
    global guess_count
    # Set the random number
    random_number = number.randint(1, 100)
    
    while guess_count < max_guesses:
        print("Guess a number between 1 and 100. \n You have", max_guesses - guess_count, "guesses left.")
        try:
            user_guess = int(input("Enter your guess: "))
            guess_count += 1
            print("You guessed", user_guess)

            if user_guess < random_number:
                print("Too low!")
            elif user_guess > random_number:
                print("Too high!")
            else:
                print("You guessed it!")
                return
        except ValueError:
            print("Please enter a valid number!")
            continue
    
    if guess_count == max_guesses:
        print("You ran out of guesses! The number was", random_number)

# Start the game
number_guess()


            