
from sympy import *
import numpy as np
from sympy.integrals.manualintegrate import integral_steps
from sympy.integrals.manualintegrate import manualintegrate


x = symbols('x')


def polynomial(diff=2):

    if diff == 2:
        terms = int(np.random.choice(list(range(2, 5)), 1))
        coefficient_type = list(np.random.choice(['natural', 'negative', 'fraction', 'root'], terms))
        exponent_type = list(np.random.choice(['natural', 'negative', 'fraction', 'root'], terms))
    else:
        terms = 1
        coefficient_type = ['natural']
        exponent_type = ['natural']

    coefficients = np.random.choice(list(range(1, 20)), terms)
    coefficients[coefficient_type == 'negative'] = -coefficients[coefficient_type == 'negative']
    #coefficients[coefficient_type == 'fraction'] =


    exponents = np.random.choice(list(range(0, 10)), terms, replace=False)
    exponents[exponent_type == 'negative'] = -exponents[exponent_type == 'negative']


    expr = 0
    for i in range(0, terms):
        expr += coefficients[i] * x ** (exponents[i])

    #print('alpha', coefficients)
    #print('beta', exponents)
    #print(terms)
    pprint(expr, use_unicode=True)
    return expr


polynomial()
#print(integral_steps(polynomial(),x))