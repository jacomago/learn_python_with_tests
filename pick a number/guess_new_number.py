import random

def play_game():
    number = random.randint(1, 100)

    for i in range(5):
        guess_workflow(number)
    
    print("I'm sorry you ran out of guesses.")

def guess_workflow(number):
    guess = input("Guess a number, between 1 and 100:")
    guess = int(guess)

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too big!")
    else:
        print("You got it right!")

def play_again():
    while True:
        play_choice = input("Would you like to play a game? (Y/N)")
        if play_choice == "N":
            return False
        elif play_choice == "Y":
            return True
        print("Please answer Y or N")

play_game()

while True:
    choice = play_again()
    if not choice:
        exit()
    else:
        play_game()