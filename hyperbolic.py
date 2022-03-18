from sympy import *
from sympy import init_printing
import numpy as np
from fractions import Fraction as frac

x = symbols('x')

## HYPERBOLIC FUNCTION GENERATOR

def generate_hyperbolic(difficulty = 1):

    expr = 0

    if difficulty == 1:
    ### USE ONLY SINH COSH TANH TO FIRST DEGREE WITH SCALARS
        terms = int(np.random.choice(list(range(3, 6)), 1))
        coefficient_type = np.asarray(np.random.choice(['natural', 'negative', 'fractions'], terms))
        hyperbolics = np.asarray(np.random.choice([sinh, cosh, tanh, coth, sech, csch], terms))
        coefficients = np.random.choice(list(range(1, 20)), terms)

        coefficients[coefficient_type == 'negative'] = -coefficients[coefficient_type == 'negative']
        # coefficients[coefficient_type == 'fractions'] = frac(1,  coefficients[coefficient_type == 'fractions'])

        print(coefficient_type)
        print(coefficients[coefficient_type == 'fractions'])

        for i in range(0, terms):
            # if i in coefficients[coefficient_type == 'fractions']:
            #     expr += hyperbolics[i] * 1 / coefficients[i]
            else:
                expr += coefficients[i] * hyperbolics[i](x)

    if difficulty == 2:
    ### INCLUDE COTH SECH CSCH
        terms = int(np.random.choice(list(range(1, 3)), 1))
        coefficient_type = np.asarray(np.random.choice(['natural', 'negative', 'fractions'], terms))
        hyperbolics = np.asarray(np.random.choice([sinh, cosh, tanh, coth, sech, csch], terms))
        coefficients = np.random.choice(list(range(1, 20)), terms)
        coefficients[coefficient_type == 'negative'] = -coefficients[coefficient_type == 'negative']

    return expr

expr = generate_hyperbolic(difficulty = 1)
pprint(expr, use_unicode = True)
