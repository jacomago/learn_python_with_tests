import random

number = random.randint(1, 100)

guess = input("Guess a number, between 1 and 100:")
guess = int(guess)

if guess != number:
    print("I'm sorry you got it wrong.")
else:
    print("You got it right!")