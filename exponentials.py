""" TO DO:
make difficulty more interesting
add parameter for num terms to produce and let difficulty effect the actual integral (coefficients ext)

find a way to print bases nicely
find an even prettier print
"""

from sympy import *
import numpy as np
from fractions import Fraction as frac
from sympy.integrals.manualintegrate import integral_steps

x = symbols('x')
integer_choice = range(-10, 10)


def get_fractional_coeff(int_range):
    coefficient_denominator = np.random.choice(int_range)
    coefficient_numerator = np.random.choice(int_range)
    coefficient = frac(coefficient_numerator, coefficient_denominator)
    return coefficient


def generate_polynomial(order, integer_range, architecture=None):
    terms = order + 1
    integral = 0
    if architecture == None:
        architecture = tuple(1 for _ in range(terms))

    for power, terms in enumerate(architecture):
        for j in range(terms):
            coefficient = get_fractional_coeff(integer_range)
            integral += coefficient * x**power
    return integral


def generate_exponential(difficulty, integer_range):
    integral = 0

    match difficulty:
        case 'Easy':  # simple exponential
            coefficient = get_fractional_coeff(integer_range)
            integral += coefficient * exp(x)
        case 'Medium':
            coefficient = get_fractional_coeff(integer_range)
            polynomial_ord1 = generate_polynomial(1, integer_range)
            integral += coefficient * exp(polynomial_ord1)
        case 'Hard':
            chance = 'heads' if np.random.random() >= 0.5 else 'tails'
            coefficient = get_fractional_coeff(integer_range)
            if chance == 'heads':
                polynomial_power = generate_polynomial(2, integer_range)
                polynomial_coefficient = generate_polynomial(1, integer_range)
            else:
                polynomial_power = generate_polynomial(3, integer_range)
                polynomial_coefficient = generate_polynomial(2, integer_range)
            integral += coefficient * polynomial_coefficient * exp(polynomial_power)

    return integral


def generate_ln(difficulty, integer_range):
    terms = No_of_terms[difficulty]
    integral = 0

    for i in range(terms):
        power = get_fractional_coeff(integer_range)
        coefficient = get_fractional_coeff(integer_range)
        ln_coefficient = get_fractional_coeff(integer_range)

        integral += coefficient * log(ln_coefficient * x**power)
    return integral


def generate_log(difficulty, integer_range, base):
    terms = No_of_terms[difficulty]
    integral = 0

    for i in range(terms):
        power = get_fractional_coeff(integer_range)
        coefficient = get_fractional_coeff(integer_range)
        ln_coefficient = get_fractional_coeff(integer_range)

        integral += coefficient * log(ln_coefficient * x**power, base)
    return integral


test = generate_polynomial(2, integer_choice)

solution = generate_exponential('easy', integer_range=integer_choice)
# FOR PERTY PRINTING
init_printing()
pprint(solution)
