# This game is implemented using Random module 

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python Number Guessing Game")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input(f"Enter a guess between {lowest_num} and {highest_num}: ")
    
    # Validate that the input is a valid number
    if not guess.isdigit():
        print("Invalid input. Please enter a number.")
        continue
        
    guess = int(guess)
    guesses += 1
    
    # Check if the guess is out of bounds
    if guess < lowest_num or guess > highest_num:
        print("That number is out of range!")
    # Check if the guess is too low
    elif guess < answer:
        print("Too low! Try again.")
    # Check if the guess is too high
    elif guess > answer:
        print("Too high! Try again.")
    # The guess is correct
    else:
        print(f"CORRECT! The answer was {answer}.")
        print(f"Number of guesses: {guesses}")
        is_running = False
