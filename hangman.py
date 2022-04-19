import random

def main():
    HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
        |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    |   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|   |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
        |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    /    |
        |
    =========''', '''
    +---+
    |   |
    O   |
    /|\  |
    / \  |
        |
    =========''']

    #Word bank of animals
    words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
            'coyote crow deer dog donkey duck eagle ferret fox frog goat '
            'goose hawk lion lizard llama mole monkey moose mouse mule newt '
            'otter owl panda parrot pigeon python rabbit ram rat raven '
            'rhino salmon seal shark sheep skunk sloth snake spider '
            'stork swan tiger toad trout turkey turtle weasel whale wolf '
            'wombat zebra ').split()
    
    word = random.choice(words)
    hanged = False
    letters = set()
    alphabet = [l for l in "abcdefghijklmnopqrstuvxwyz"]
    incorrect_guesses = 0    
    while not hanged:
        letters, incorrect_guesses = update_status(word, incorrect_guesses, letters)
        print_status(letters, HANGMANPICS[incorrect_guesses], alphabet, word)
        check_end_game(letters, word, len(HANGMANPICS))

def check_end_game(letters, word, n):
    if win(letters, word):
        print("You won!")
    elif lost(letters, n):
        print("Sorry you lost.")
    else:
        return
    print("The word was:", word)
    exit()

def update_status(word, incorrect_guesses, letters):
    guess = input("Letter?")
    if guess not in word:
        incorrect_guesses += 1
    letters.add(guess)
    return letters, incorrect_guesses

def letter_status(letters, l):
    if l in letters:
        return l
    else:
        return "_"

def word_status(letters, word):
    return "".join(letter_status(letters, l) for l in word)

def win(letters, word):
    if len([l for l in word if l not in letters]) == 0:
        return True
    return False

def lost(letters, n):
    if len(letters) == n:
        return True
    return False

def print_status(letters, pic, alphabet, word):
    print("Letters guessed: ", "".join(letters))
    print("Letters left:", "".join(l for l in alphabet if l not in letters))
    print(pic)
    print(word_status(letters, word))

main()