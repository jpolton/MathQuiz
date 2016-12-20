import random
import os.path # query existance of score file name
import time # timer function
import numpy as np # Score data reading and handling
from tabulate import tabulate # pretty tabular data

"""
19 Dec 2016: jpolton. Adapted from Lewis Cornwall: http://codereview.stackexchange.com/questions/23678/hangman-in-python

To do:
* Read words from dictionary
* implement level settings choosing correct word based on possible permutations: http://stackoverflow.com/questions/15936937/given-a-list-of-words-how-to-put-them-into-families

"""
###################################

def play(word):
    HANGMAN = [
    '  +---+   \n  |   |   \n      |   \n      |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n      |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n  |   |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|   |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n      |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n /    |   \n      |   \n========= \n',
    '  +---+   \n  |   |   \n  0   |   \n /|\\  |   \n / \\  |   \n      |   \n========= \n'
    ]

    MAX = len(HANGMAN) - 1
#    WORDS = ('jazz', 'buzz', 'hajj', 'fuzz', 'jinx', 'jazzy', 'fuzzy', 'faffs', 'fizzy', 'jiffs', 'jazzed', 'buzzed', 'jazzes', 'faffed', 'fizzed', 'jazzing', 'buzzing', 'jazzier', 'faffing', 'fuzzing')
    sizeHangman = 0
#    word = random.choice(WORDS)
    hiddenWord = list('-' * len(word))
    requiredGuesses = set(word)
    lettersGuessed = [] # Don't want this to be a set(), because want it ordered for listing

    print('\tHANGMAN GAME\n\t\tBy Lewis Cornwall\n\thttp://codereview.stackexchange.com/questions/23678/hangman-in-python')
    while sizeHangman < MAX:
        hiddenWord = ''.join('-' if l in requiredGuesses else l for l in word)
        print('This is your hangman:\n' + HANGMAN[sizeHangman] +
            '\nThis is the word:\n' + ''.join(hiddenWord) +
            '\nThese are the letters you\'ve already guessed:\n' +
            ", ".join(str(e) for e in lettersGuessed))

        guess = raw_input('Guess a letter: ').lower()
        # Process guess
        if guess in lettersGuessed:
            print('You already guessed this')
        elif guess in requiredGuesses:
            print('Correct guess!')
            requiredGuesses.remove(guess)
            lettersGuessed.append(guess)
        else:
            print('Incorrect guess')
            lettersGuessed.append(guess)
            sizeHangman += 1

        if not requiredGuesses:
            print('You found the word:\n')
            print(word.upper())
            print('\n')
            break

    else:
        print('This is your hangman:\n' + HANGMAN[sizeHangman] +
            '\nThis is the word:\n' + ''.join(hiddenWord) +
            '\nYou\'ve been hanged! My work was actaully ' + word.upper() +'\n')

    return len(word)

def load_words():
    words = []
    with open("dictionary.txt") as file:
        words = file.readlines()
    return [word.strip() for word in words]


def identify_user():
    user_name = raw_input("Enter your initial: ").upper()
    if (user_name == "" or user_name == "E"):
        user_name = "E"
        print("Hello E!")
        level = 10
    elif user_name == "J":
        print("Hello Daddy!")
        level = 100
    elif user_name == "Y":
        print("Hello Mummy!")
        level = 100
    else:
        print("Nice to meet you ", user_name)
        level = 10
    # Create a score file if it doesn't exist
    filename = "hangman_" + user_name + "_" + str(level) + ".txt"
    if not os.path.isfile(filename):
        target = open(filename, 'w')
        target.write( '%s %s' % ('Score', 'Time(s)') )
        target.write('\n')
        target.close()
    return user_name, level

def save_score(user_name, level, score, time):
    filename = "hangman_" + user_name + "_" + str(level) + ".txt"
    target = open(filename, 'a')
    target.write( '%d %d' % (score, time) )
    target.write('\n')
    target.close()
    return

def display_score(user_name, level):
    filename = "hangman_" + user_name + "_" + str(level) + ".txt"
    target = open(filename, 'r')
    stuff = np.loadtxt(target, skiprows=1)
    print tabulate(stuff,headers=('Score','Time (s)'))
    print('Average score: {}'.format( round(np.mean(stuff[:,0]),1)) )
    print('\n')
    target.close()
    return

def menu():
    print "-----HANGMAN GAME-----"
    print "1. Play game"
    print "2. Display score"
    print "3. Exit"

    user_input = float(input("Choose an option: "))
    return user_input

###################################

def main():
    user_name, level = identify_user()
    while True:
        menu_choice = menu()

        if menu_choice == 1:      # play game
            words = load_words()
            start = time.time()
            score = play(random.choice(words))
            end = time.time()
            duration = int(round(end-start))
            print('{user_name}, you found the {score} letter word in {duration} seconds'.format(**locals()))
            print('\n')
            save_score(user_name, level, score, duration )

        elif menu_choice == 2:        # Display score
            display_score(user_name, level)

        elif menu_choice == 3:      # Exit
            break

        else:
            print("Sorry, I don't understand. Please try again...")
            print()

if __name__ == '__main__':
    main()
