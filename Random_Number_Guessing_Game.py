#this is a random number guessing-game. the user defines the range and the number of guesses
import random

try:
    lower_bound = int(input("Enter the lower bound of the range to guess: "))
except:
    print("Please enter a number for the lower bound")
try:
    upper_bound = int(input("Enter the upper bound of the range to guess: "))
except:
    print("Please enter a number for the upper bound")

try:
    num_guesses = int(input("Enter number of guesses you want: "))
except:
    print("Please enter a number for the guesses allowed")


num_tries = num_guesses #this is used to display the number of tries used if user doesn't guess correctly
if lower_bound > upper_bound:
    print("Enter an upper bound that is larger than the lower bound!")
else:
    x = random.randint(lower_bound, upper_bound)
    while num_guesses > 0:
        num_guesses -= 1
        y = int(input(f"Guess a number between {lower_bound} & {upper_bound}: "))
        if x == y:
            print(f"You guessed it! the number was {y}")
            break
        if x < y:
            print(f"Your guess of {y} was too large")
        if x > y:
            print(f"Your guess of {y} was too small")

    if num_guesses == 0:
        print(f"The number was {x}, all {num_tries} guesses used up!")

