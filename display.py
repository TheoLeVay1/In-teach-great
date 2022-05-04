from sympy import *
import numpy as np
from expressionGeneratorV2 import *
import matplotlib.pyplot as plt
import random

x = symbols('x')
c = symbols('c')

def display_question_def_int(integrand):
    lim1, lim2 = 0,0
    while lim1 == lim2:
        lim1 = np.random.randint(-10, 10)
        lim2 = np.random.randint(-10, 10)
    limits = np.array([lim1, lim2])
    limits.sort()

    dummy_limits1 = limits + 1
    dummy_limits2 = limits - 2

    question = Integral(integrand, (x, limits[0], limits[1]))
    dummy_q1 = Integral(integrand, (x, dummy_limits1[0], dummy_limits1[1]))
    dummy_q2 = Integral(integrand, (x, dummy_limits2[0], dummy_limits2[1]))

    solution = question.doit()
    inc_sol1 = -solution
    inc_sol2 = dummy_q1.doit()
    inc_sol3 = dummy_q2.doit()  # maybe make this -inc_sol2 so its not obvious what the correct sol is

    all_choice = [solution, inc_sol1, inc_sol2, inc_sol3]
    for i, choice in enumerate(all_choice[1:]):
        if choice == solution:
            while choice == solution:
                choice = np.random.randint(-100, 100)
            all_choice[i+1] = choice

    random.shuffle(all_choice)
    for i, choice in enumerate(all_choice):
        if choice == solution:
            corr_choice = i
            break

    quest_pos = (0.5, 5/6)
    a_pos = (0.25, 3/6)
    b_pos = (0.75, 3/6)
    c_pos = (0.25, 1/6)
    d_pos = (0.75, 1/6)
    positions = np.array([[a_pos, b_pos, c_pos, d_pos],['a', 'b', 'c', 'd']])

    fig = plt.figure()
    plt.text(*quest_pos, r"$%s$" % latex(question), ha='center',fontsize=21)
    for i in range(4):
        plt.text(*positions[0,i], f"{positions[1,i]})\t" r"$%s$" % latex(all_choice[i]), ha='center',fontsize=14)
    ax = fig.get_axes()[0]
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    return positions[1,corr_choice]

test = generate_basic_polynomial(difficulty='Easy')
display_question_def_int(test)
print('yay')


def display_question_indef_int(integrand):
    question = Integral(integrand)
    solution = integrate(integrand)
    differential = diff(integrand)

    corr_sol = solution + c
    inc_sol_1 = solution
    inc_sol_2 = differential + c
    inc_sol_3 = differential
    multi_choice = [corr_sol, inc_sol_1, inc_sol_2, inc_sol_3]
    random.shuffle(multi_choice)
    for i, choice in enumerate(multi_choice):
        if choice == corr_sol:
            corr_choice = i
    # 1:a 2:b 3:c 4:d

    quest_pos = (0.5, 5/6)
    a_pos = (0.25, 3/6)
    b_pos = (0.75, 3/6)
    c_pos = (0.25, 1/6)
    d_pos = (0.75, 1/6)
    positions = np.array([[a_pos, b_pos, c_pos, d_pos],['a', 'b', 'c', 'd']])

    fig = plt.figure(figsize=(8,8))
    plt.text(*quest_pos, r"$%s$" % latex(question), ha='center',fontsize=21)
    for i in range(4):
        plt.text(*positions[0,i], f"{positions[1,i]})\t" r"$%s$" % latex(multi_choice[i]), ha='center',fontsize=14)
    ax = fig.get_axes()[0]
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()

    return positions[1,corr_choice]


polynomial = generate_basic_polynomial('Medium')
corr_sol = display_question_indef_int(polynomial)
print('yay')

question = Integral(polynomial)
solution_1 = integrate(polynomial, x)
solution_2 = diff(polynomial)
solution_3 = solution_2 + c
solution = solution_1 + c

quest_latex = latex(question)
sol1_latex = latex(solution_1)
sol2_latex = latex(solution_2)
sol3_latex = latex(solution_3)
solution_latex = latex(solution) 

quest_pos = (0.5, 5/6)
a_pos = (0.25, 3/6)
b_pos = (0.75, 3/6)
c_pos = (0.25, 1/6)
d_pos = (0.75, 1/6)

fig = plt.figure(figsize=(8,8))
plt.text(*quest_pos, r"$%s$" % quest_latex, ha='center',fontsize=21)
plt.text(*a_pos, r"$%s$" % solution_latex, ha='center',fontsize=14)
plt.text(*c_pos, r"$%s$" % sol1_latex, ha='center',fontsize=14)
plt.text(*b_pos, r"$%s$" % sol2_latex, ha='center',fontsize=14)
plt.text(*d_pos, r"$%s$" % sol3_latex, ha='center',fontsize=14)
ax = fig.get_axes()[0]
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
#plt.text(0.1, 0.5, r"$%s$" % poly_int_latex, fontsize=21)
plt.show()

latex_to_img(poly_latex).save('img.png')
print('yay')

