""" TO DO:
make difficulty more interesting
add parameter for num terms to produce and let difficulty effect the actual integral (coefficients ext)
"""

from sympy import *
import numpy as np
from fractions import Fraction as frac
from sympy.integrals.manualintegrate import integral_steps

x = symbols('x')
integer_choice = range(1, 21)
No_of_terms = {'hard': 3, 'easy': 1}


def get_fractional_coeff(range):
    coefficient_denominator = np.random.choice(range)
    coefficient_numerator = np.random.choice(range)
    coefficient = frac(coefficient_numerator, coefficient_denominator)
    return coefficient


def generate_exponential(difficulty, integer_range):
    terms = No_of_terms[difficulty]
    integral = 0

    for i in range(terms):
        coefficient = get_fractional_coeff(integer_range)
        exp_coefficient = get_fractional_coeff(integer_range)
        exp_power = get_fractional_coeff(integer_range)

        integral += coefficient * exp(exp_coefficient * x**exp_power)

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


solution = generate_exponential('easy', integer_range=integer_choice)
print(solution)
