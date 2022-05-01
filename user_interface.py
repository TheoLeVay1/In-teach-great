from sympy import *
import numpy as np
import random
from expressionGenerator import polynomial


def multi_choice(topic, difficulty, choices):
    """
    Gives a multiple choice question

    :param topic: function
            What area of maths wants to be covered. (I.e polynomials, trigonometric, etc)
    :param difficulty: integer
            Difficulty for the area of maths. Range (1-3)
    :param choices: integer
            Number of choices in the multiple choice
    :return:
    """

    # Set up question
    question = topic(difficulty)
    correct_solution = integrate(question)

    # Set up letters for choices
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

    # Can't have too many options
    if choices > 9:
        raise ValueError("Number of choices is too large")

    # Set up lists for solution collection
    answers = [0]*choices
    answers[0] = correct_solution
    answer_letters = [' ']*choices
    answer_letters[0] = 'A'

    # Create dummy solutions from same pool of questions with same difficulty
    for i in range(1, choices):
        solution = integrate(topic(difficulty))
        answers[i] = solution
        answer_letters[i] = alphabet[i]

    # Shuffle the solution and dummy solutions
    random.shuffle(answers)

    # Print out questions and solution choices
    print("Question: \n")
    pprint(question, use_unicode=True)
    print(" \n==========================================")
    print("\nSolutions: ")

    for i in range(len(answers)):
        print('Answer ' + str(answer_letters[i]) + ': ')
        pprint(answers[i], use_unicode=True)
        print("\n")

    # Get user's answer
    valid_answer = False
    user_answer = ''
    while not valid_answer:
        user_answer = input('What is the integral to the question? (type in the letter of the answer)')
        if user_answer in answer_letters:
            valid_answer = True
        else:
            print('Your input is not a letter of one of the choices')
    answer_index = answer_letters.index(user_answer)
    selected_answer = answers[answer_index]

    if selected_answer == correct_solution:
        print('correct!')
    else:
        print('Incorrect :(')
        print('The correct answer was: ' + str(correct_solution))


if __name__ == '__main__':
    # Example of a multiple choice for polynomials of difficulty 3 and there being 4 choices
    multi_choice(polynomial, 3, 4)
