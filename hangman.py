import random

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
WORDS = ('jazz', 'buzz', 'hajj', 'fuzz', 'jinx', 'jazzy', 'fuzzy', 'faffs', 'fizzy', 'jiffs', 'jazzed', 'buzzed', 'jazzes', 'faffed', 'fizzed', 'jazzing', 'buzzing', 'jazzier', 'faffing', 'fuzzing')
sizeHangman = 0
word = random.choice(WORDS)
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
