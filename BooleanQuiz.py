"""Run this script: $ python3 BooleanQuiz.py WelcomePrompt.txt AnswerSheet.txt"""
from random import sample
from sys import argv
script, file_1, file_2 = argv
import QuestionBank

correct_answers = 0    # Use to increment correct answers
incorrect_answers = 0  # Use to increment incorrect answers
question_number = 1    # Use to increment question numbers while taking quiz
question_count = 2     # Number of questions to ask in this quiz
random_numbers = sample(range(len(QuestionBank.question_bank)),question_count)
# Generate random integers within the question_bank list's range


def welcome_prompt(f):
    """A function that prints a 'Welcome Prompt' for the user"""
    print("\033c")        # Clear the terminal screen for the user
    open_f = open(f)      # Open the input_file_1 (WelcomePrompt.txt)
    print (open_f.read()) # Print .txt file to the terminal
    open_f.close()        # Close the opened input_file_1
    ready = input("Are you ready? Press ENTER key to begin.\n>>>")

welcome_prompt(file_1) # Call function that prints out the Welcome Prompt


while question_count > 0:
    """A function that generates random questions from the question bank"""
    print("\033c")             # Clear the terminal screen for the user
    question = QuestionBank.question_bank[random_numbers.pop(0)] # Parse random tuple from question_bank
    print ("%r) Does the following expression result in True or False?\n\t" % question_number, question[0])
    answer = input(">>>")
    if answer == question[1]:  # Compare user's answer to correct answer in "question" tuple
        correct_answers += 1   # Increment correct answer from user
        print ("\nCorrect!")
    else:
        incorrect_answers += 1 # Increment incorrect answer from user
        print ("\nSorry, that's incorrect.")
    print (input("\nSo far, you have answered %d correct, and %d wrong. Press ENTER key to continue.\n>>>" % (correct_answers, incorrect_answers)))
    question_count -= 1        # Decrement qty of questions left
    question_number += 1       # Increment question number


def final_score():
    """A function that prints the final score"""
    print("\033c") # Clear the terminal screen for the user
    score = (correct_answers / (correct_answers + incorrect_answers))
    print ("Thanks for taking the quiz! Your final score is: {:.1%}".format(score))
    print (input("\nPress ENTER key to see the answer key.\n>>>"))


def print_answer_sheet(f):
    """A function that prints out the answer key"""
    print("\033c")        # Clears the terminal screen for the user
    open_f = open(f)      # Open the input_file (AnswerSheet.txt)
    print (open_f.read()) # Print .txt file to the terminal
    open_f.close()        # Close the opened input_file_2

final_score()              # Call function that prints the final score
print_answer_sheet(file_2) # Call function that prints the answer sheet
