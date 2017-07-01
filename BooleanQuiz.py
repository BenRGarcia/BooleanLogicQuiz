"""
Boolean Logic Quiz Program
Replaces the need for index/flash cards to study
Run this script with: $ python3 BooleanQuiz.py AnswerSheet.txt
"""

from random import sample
from sys import argv
script, input_file = argv

print("\033c") # Clears the terminal screen for the user

print ("""
==========================================
    Welcome to the Boolean Logic Quiz!
==========================================  \n\n
Your job is to determine whether the logic
argument will return 'True' or 'False'.\n\n
Beware!
Your inputs are case sensitive...
Remember to capitalize 'T'rue and 'F'alse!\n
""")

ready = input("Are you ready? Press any key to begin.\n>>>")

question_bank = [ # list of Boolean arguments and True/False result
("not False", "True"),
("not True", "False"),
("True or False", "True"),
("True or True", "True"),
("False or True", "True"),
("False or False", "False"),
("True and False", "False"),
("True and True", "True"),
("False and True", "False"),
("False and False", "False"),
("not(True or False)", "False"),
("not(True or True)", "False"),
("not(False or True)", "False"),
("not(False or False)", "True"),
("not(True and False)", "True"),
("not(True and True)", "False"),
("not(False and True)", "True"),
("not(False and False)", "True"),
("1 != 0", "True"),
("1 != 1", "False"),
("0 != 1", "True"),
("0 != 0", "False"),
("1 == 0", "False"),
("1 == 1", "True"),
("0 == 1", "False"),
("0 == 0", "True")
]


question_count = 8 # Number of questions to ask in this quiz
random_numbers = sample(range(26),question_count) # Use to randomize quiz questions
correct_answers = 0    # Use to increment correct answers
incorrect_answers = 0  # Use to increment incorrect answers
number = 1             # Use to incrememt question numbers


while question_count > 0:
    """A function that asks random questions from the question bank"""
    print("\033c") # Clears the terminal screen for the user
    question = question_bank[random_numbers.pop(0)]
    print ("\n%r) Does the following expression result in True or False?\n\t" % number, question[0])
    answer = input(">>>")
    number += 1 # increment question number
    if answer == question[1]:
        correct_answers += 1 # increment a correct answer from user
        print ("\nCorrect!")
    else:
        incorrect_answers += 1 # increment an incorrect answer from user
        print ("\nSorry, that's incorrect.")
    print ("\nSo far, you have answered %d correct, and %d wrong." % (correct_answers, incorrect_answers))
    next_question = input("\nPress any key to continue.\n>>>")
    question_count -= 1

print("\033c") # Clears the terminal screen for the user

def final_score():
    """A function that prints the final score"""
    score = (correct_answers / (correct_answers + incorrect_answers)) * 100
    print ("\nYour final score is: %d" % score)

final_score()


print ("\nThanks for taking the quiz! Press any key to see the answer key.")
next_question = input(">>>")

def print_answer_sheet(f):
    """A function that prints out the answer key"""
    print("\033c") # Clears the terminal screen for the user
    print ("\n\nHere is the answer key:\n\n", f.read())


open_input_file = open(input_file)  # Open the input_file (ex27_answerkey.txt)
print_answer_sheet(open_input_file) # Call function that prints the answer sheet
open_input_file.close()             # Close the input_file
