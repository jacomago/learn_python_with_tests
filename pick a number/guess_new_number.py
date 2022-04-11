import random

def guess_workflow(number):
    guess = input("Guess a number, between 1 and 100:")
    guess = int(guess)

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("You got it right!")

number = random.randint(1, 100)

for i in range(5):
    guess_workflow(number)

print("I'm sorry you ran out of guesses.")