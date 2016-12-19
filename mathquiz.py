import operator
import random
import time
import os.path # query existance of score file name
from tabulate import tabulate # pretty tabular data
import numpy as np # Score data reading and handling

"""
19 Dec 2016: jpolton. Adapted from discussion: http://codereview.stackexchange.com/questions/77299/math-equation-generator-program
dan0117: http://codereview.stackexchange.com/users/62824/dan0117
200_success: http://codereview.stackexchange.com/users/9357/200-success

To do:
* move scores into single dictionary file
* implement sequence completion testing? 
"""

OPERATIONS = [
    ('+', operator.add),
    ('-', operator.sub),
#    ('*', operator.mul),
]

def random_question(binary_operations, operand_range):
    """Generate a pair consisting of a random question (as a string)
    and its answer (as a number)"""
    op_sym, op_func = random.choice(binary_operations)
    n1 = random.randint(min(operand_range), max(operand_range))
    n2 = random.randint(min(operand_range), max(operand_range))
    question = '{} {} {}'.format(n1, op_sym, n2)
    answer = op_func(n1, n2)
    return question, answer

def quiz(number_of_questions,level):
    """Ask the specified number of questions, and return the number of correct
    answers, for the specified difficulty level."""
    tries = 1
    score = 0
    for _ in range(number_of_questions):
        question, answer = random_question(OPERATIONS, range(0, level+1))
        user_input = float(input('What is {} ? '.format(question)))
	while (user_input != answer and tries < 3):
	    user_input = float(input('Try again. What is {} ? '.format(question)))
            tries += 1
        if answer == user_input:
            print("Correct!\n")
            score += 1
        else:
	    print('{} = {}'.format(question, answer))
	    print('\n')
    return score

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
    filename = "mathquiz_" + user_name + "_" + str(level) + ".txt"
    if not os.path.isfile(filename):
        target = open(filename, 'w')
        target.write( '%s %s' % ('Score', 'Time(s)') )
        target.write('\n')
        target.close()
    return user_name, level

def display_score(user_name, level):
    filename = "mathquiz_" + user_name + "_" + str(level) + ".txt"
    target = open(filename, 'r')
    stuff = np.loadtxt(target, skiprows=1)
    print tabulate(stuff,headers=('Score','Time (s)'))
    print('Average score: {}'.format( round(np.mean(stuff[:,0]),1)) )
    print('\n')
    target.close()
    return

def save_score(user_name, level, score, time):
    filename = "mathquiz_" + user_name + "_" + str(level) + ".txt"
    target = open(filename, 'a')
    target.write( '%d %d' % (score, time) )
    target.write('\n')
    target.close()
    return

def menu():
    print "-----MATHS QUIZ-----"
    print "1. Play game"
    print "2. Display score"
    print "3. Exit"

    user_input = float(input("Choose an option: "))
    return user_input

def main():
    user_name, level = identify_user()
    while True:
        menu_choice = menu()
        if menu_choice == 2:        # Display score
            display_score(user_name, level)

        elif menu_choice == 1:      # Run quiz
	    QUESTIONS = 10
            start = time.time()
            score = quiz(QUESTIONS, level)
            end = time.time()
            print('{user_name}, you scored {score} out of {QUESTIONS}'.format(**locals()))
            print('\n')
	    save_score(user_name,  level, score, int(round(end-start)) )

        elif menu_choice == 3:      # Exit
            break

        else:
            print("Sorry, I don't understand. Please try again...")
            print()

if __name__ == '__main__':
    main()
