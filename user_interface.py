from sympy import *
import numpy as np
import random
from expressionGenerator import polynomial

# Set up question
difficulty = 3
q1 = polynomial(difficulty)
solution_1 = integrate(q1)
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
number_of_choice = 4
if number_of_choice > 9:
    raise ValueError("Number of choices is too large")
answers = [0]*number_of_choice
answers[0] = solution_1
answer_letters = [' ']*number_of_choice
answer_letters[0] = 'A'
for i in range(1, number_of_choice):
    solution = integrate(polynomial(difficulty))
    answers[i] = solution
    answer_letters[i] = alphabet[i]

random.shuffle(answers)
print("Question: ")
pprint(q1, use_unicode=True)
print("\nsolutions: \n")


for i in range(len(answers)):
    print('Answer ' + str(answer_letters[i]) + ': ')
    pprint(answers[i], use_unicode=True)
    print("\n")

user_answer = input('Is the solution A, B, C or D?')
answer_index = answer_letters.index(user_answer)
selected_answer = answers[answer_index]

if selected_answer == solution_1:
    print('correct!')
else:
    print('Incorrect :(')
    print('The correct answer was: ' + str(solution_1))

