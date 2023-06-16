import random
import sys


def main():
    # Word bank of animals
    words = (
        "ant baboon badger bat bear beaver camel cat clam cobra cougar "
        "coyote crow deer dog donkey duck eagle ferret fox frog goat "
        "goose hawk lion lizard llama mole monkey moose mouse mule newt "
        "otter owl panda parrot pigeon python rabbit ram rat raven "
        "rhino salmon seal shark sheep skunk sloth snake spider "
        "stork swan tiger toad trout turkey turtle weasel whale wolf "
        "wombat zebra "
    ).split()
    max_word_length = max([len(word) for word in words])
    word_dict = {
        n: [word for word in words if len(word) == n]
        for n in range(3, max_word_length + 1)
    }
    word_length = 5
    words = word_dict[word_length]

    print(
        "Hello, welcome to wordle. You must guess the correct ",
        word_length,
        "letter length word.",
    )
    c_mod = "*"
    p_mod = "_"
    print(
        "If you get the correct place, you will see ", c_mod, "surrounding the letter."
    )
    print(
        "If you get the correct letter but wrong place, you will see ",
        p_mod,
        "surrounding the letter.",
    )

    word = random.choice(words)
    hanged = False
    allowed_guesses = 6
    all_correct, all_wrong_place, all_wrong = set(), set(), set()
    alphabet = list("abcdefghijklmnopqrstuvxwyz")
    previous_guesses_status = []
    while not hanged:
        all_correct, all_wrong_place, all_wrong, print_guess, guess = update_status(
            words, word, all_correct, all_wrong_place, all_wrong
        )
        previous_guesses_status.append(print_guess)

        print_status(
            all_correct, all_wrong_place, all_wrong, alphabet, previous_guesses_status
        )

        check_end_game(guess, word, allowed_guesses)


def update_status(words, word, all_correct, all_wrong_place, all_wrong):
    guess = get_guess(words)

    correct, wrong_place, wrong = get_word_status(word, guess)
    print_guess = print_word_status(guess, correct, wrong_place)

    all_correct = all_correct | correct
    all_wrong_place = (all_wrong_place | wrong_place) - all_correct
    all_wrong = all_wrong | wrong

    return all_correct, all_wrong_place, all_wrong, print_guess, guess


def check_end_game(guess, word, n):
    if win(guess, word):
        print("You won!")
    elif lost(guess, n):
        print("Sorry you lost.")
    else:
        return
    print("The word was:", word)
    sys.exit()


def get_guess(words):
    print("Please guess a word.", end=" ")
    while True:
        guess = input("Your word is?")
        print("Your guess is ", guess)
        if guess.lower() in words:
            break
        print("Please guess a word from word the list.")
    return guess


def get_word_status(word, guess):
    correct = set()
    wrong_place = set()
    wrong = set()
    for index in range(len(guess)):
        letter = guess[index]
        if word[index] == letter:
            correct.add(letter)
        elif letter in word:
            wrong_place.add(letter)
        else:
            wrong.add(letter)
    return correct, wrong_place, wrong


def letter_status(letter, correct, wrong_place):
    if letter in correct:
        return "*" + letter + "*"
    elif letter in wrong_place:
        return "_" + letter + "_"
    else:
        return letter


def print_word_status(guess, correct, wrong_place):
    output = ""
    for letter in guess:
        output += " " + letter_status(letter, correct, wrong_place)
    return output


def win(letters, word):
    if len([letter for letter in word if letter not in letters]) == 0:
        return True
    return False


def lost(letters, n):
    if len(letters) == n:
        return True
    return False


def print_status(
    all_correct, all_wrong_place, all_wrong, alphabet, previous_guesses_status
):
    print(
        "Letters guessed correct: ",
        "".join(all_correct),
        " Letters guessed in wrong place still: ",
        "".join(all_wrong_place),
        " Letters guessed wrong: ",
        "".join(all_wrong),
    )
    print(
        "Letters left:",
        "".join(
            letter
            for letter in alphabet
            if letter not in (all_correct | all_wrong_place | all_wrong)
        ),
    )
    print("Previous guesses:")
    for guess in previous_guesses_status:
        print(guess)


main()
