import random
import sys


def get_ranges():
    guesses = int(input("How many guesses allowed?"))
    a = int(input("Minimum number?"))
    b = int(input("Maximum number?"))
    return a, b, guesses


def play_game(a, b, guesses):
    number = random.randint(a, b)
    for _i in range(guesses):
        if guess_workflow(number, a, b):
            return

    print("I'm sorry you ran out of guesses., you are dumb")


def guess_workflow(number, a, b):
    guess = input("Guess a number, between " + str(a) + " and " + str(b) + ":")
    guess = int(guess)

    if guess < number:
        print("Too small!")
        return False
    elif guess > number:
        print("Too big!")
        return False
    else:
        print("You got it right!")
        return True


def play_again():
    while True:
        play_choice = input("Would you like to play again? (Y/N)")
        if play_choice == "N":
            return False
        elif play_choice == "Y":
            return True
        print("Please answer Y or N")


def main():
    ranges = get_ranges()
    play_game(*ranges)

    while True:
        choice = play_again()
        if not choice:
            sys.exit()
        else:
            ranges = get_ranges()
            play_game(*ranges)
