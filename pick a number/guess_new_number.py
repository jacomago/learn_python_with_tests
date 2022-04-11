import random

number = random.randint(1, 100)

for i in range(5):
    guess = input("Guess a number, between 1 and 100:")
    guess = int(guess)

    if guess != number:
        print("I'm sorry you got it wrong, try again.")
    else:
        print("You got it right!")

print("I'm sorry you ran out of guesses.")