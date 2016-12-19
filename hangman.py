import random
HANGMAN = (
'''
-------+''',
'''
       +
       |
       |
       |
       |
       |
-------+''',
'''
  -----+
       |
       |
       |
       |
       |
-------+''',
'''
  -----+
  |    |
       |
       |
       |
       |
-------+''',
'''
  -----+
  |    |
  O    |
       |
       |
       |
-------+''',
'''
  -----+
  |    |
  O    |
  |    |
       |
       |
-------+''',
'''
  -----+
  |    |
  O    |
 /|    |
       |
       |
-------+''',
'''
  -----+
  |    |
  O    |
 /|\   |
       |
       |
-------+''',
'''
  -----+
  |    |
  O    |
 /|\   |
 /     |
       |
-------+''',
'''
  -----+
  |    |
  O    |
 /|\   |
 / \   |
       |
-------+''')
MAX = len(HANGMAN) - 1
WORDS = ('jazz', 'buzz', 'hajj', 'fuzz', 'jinx', 'jazzy', 'fuzzy', 'faffs', 'fizzy', 'jiffs', 'jazzed', 'buzzed', 'jazzes', 'faffed', 'fizzed', 'jazzing', 'buzzing', 'jazzier', 'faffing', 'fuzzing')
sizeHangman = 0
word = random.choice(WORDS)
hiddenWord = list('-' * len(word))
lettersGuessed = []
print('\tHANGMAN GAME\n\t\tBy Lewis Cornwall\n\thttp://codereview.stackexchange.com/questions/23678/hangman-in-python')
while sizeHangman < MAX:
    print('This is your hangman:' + HANGMAN[sizeHangman] + '\nThis is the word:\n' + ''.join(hiddenWord) + '\nThese are the letters you\'ve already guessed:\n' + str(lettersGuessed))
    while True:
        guess = raw_input('Guess a letter: ').lower()
        if guess in lettersGuessed:
            print('You\'ve already guessed that letter!')
        else:
            break
    if guess in word:
        print('Well done, "' + guess + '" is in my word!')
        for i, letter in enumerate(word):
            if guess == letter:
                hiddenWord[i] = guess
        if '-' not in hiddenWord:
            print('Congratulations! My word was ' + word + '!')
            break
    else:
        print('Unfortunately, "' + guess + '" is not in my word.')
        sizeHangman += 1
    lettersGuessed.append(guess)
else:
    print('This is your hangman: ' + HANGMAN[sizeHangman] + 'You\'ve been hanged! My word was actually ' + word + '.')
input('Press <enter> to close.')
