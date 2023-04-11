# Player must guess the number and has 6 tries before gameover.
import random

player = input('Hello! What is your name? ')
random_number = random.randint(1,20)
print(f'Ok {player}, I\'m thinking of a number between 1 and 20.')
num_of_guesses = 0
while num_of_guesses < 6:
    guess = int(input('Take a guess at the number. '))
    num_of_guesses = num_of_guesses + 1
    if guess == random_number:
        break
    elif guess < random_number:
        print(f'{guess} is too low, try again.')
    elif guess > random_number:
        print(f'{guess} is too high, try again.')
    else:
        print(f'{guess} is not a valid guess... The clock is still ticking.')

if guess == random_number:
    print(f'Great work {player}, you guessed the number in {num_of_guesses} tries!')

if guess != random_number:
    print(f'Too bad {player}, you took 6 guesses but still couldn\'t guess my number. Better luck next time.')
