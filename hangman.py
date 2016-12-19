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
#lettersGuessed = []
requiredGuesses = set(word)
lettersGuessed = set()

print('\tHANGMAN GAME\n\t\tBy Lewis Cornwall\n\thttp://codereview.stackexchange.com/questions/23678/hangman-in-python')
while sizeHangman < MAX:
    hiddenWord = ''.join('-' if l in requiredGuesses else l for l in word)
    print('This is your hangman:\n' + HANGMAN[sizeHangman] +
        '\nThis is the word:\n' + ''.join(hiddenWord) +
        '\nThese are the letters you\'ve already guessed:\n' +
         str(lettersGuessed))
#    while True:
    guess = raw_input('Guess a letter: ').lower()

    # then later
    if guess in lettersGuessed:
        print('You already guessed this')
    elif guess in requiredGuesses:
        print('Correct guess!')
        requiredGuesses.remove(guess)
        lettersGuessed.add(guess)
    else:
        print('Incorrect guess')
        lettersGuessed.add(guess)
        sizeHangman += 1

    if not requiredGuesses:
        print('You found the word:\n')
        print(word.upper())
        print('\n')
        break
    else:
        print('stuff')
#        print(''.join('-' if l in requiredGuesses else l for l in word))


else:
    print('This is your hangman:\n' + HANGMAN[sizeHangman] + 'You\'ve been hanged! My word was actually ' + word + '.')
input('Press <enter> to close.')
