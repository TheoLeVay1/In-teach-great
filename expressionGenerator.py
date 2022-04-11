
from sympy import *
import numpy as np
from random import random
from sympy.integrals.manualintegrate import integral_steps
from sympy.integrals.manualintegrate import manualintegrate


x = symbols('x')

"""
Polynomial (diff): Generates a polynomial expression
    diff = 1: Single term. Coefficients and exponents are natural numbers
    diff = 2: Two or three terms. Coefficients and exponents are natural or negative numbers
    diff = 3: Half the times it is a multiplication between two diff=2 polynomials, the other half it is a division 
        of a diff=2 polynomial by a diff=1 polynomial.
    diff = 4: Two to four terms. Coefficients can be natural numbers, negative numbers, fractions or roots. 
        Exponents can be natural numbers, negative numbers or fractions.
"""

def polynomial(diff=3):

    if diff == 4:
        terms = int(np.random.choice(list(range(2, 5)), 1))
        coefficient_type = list(np.random.choice(['natural', 'negative', 'fraction', 'root'], terms))
        exponent_type = list(np.random.choice(['natural', 'negative', 'fraction'], terms))
    elif diff == 1:
        terms = 1
        coefficient_type = ['natural']
        exponent_type = ['natural']
    elif diff == 2:
        terms = int(np.random.choice(list(range(2, 4)), 1))
        coefficient_type = list(np.random.choice(['natural', 'negative'], terms))
        exponent_type = list(np.random.choice(['natural', 'negative'], terms))

    if diff != 3:

        coefficients = [None]*terms

        for t in range(0,terms):

            if coefficient_type[t]=='natural':
                coefficients[t]=int(np.random.choice(list(range(1, 20)), 1))
            elif coefficient_type[t]=='negative':
                coefficients[t] = int(np.random.choice(list(range(-20, -1)), 1))
            elif coefficient_type[t]=='fraction':
                frac_coeff = list(np.random.choice(list(range(1, 20)), 2))
                coefficients[t] = Rational(min(frac_coeff), max(frac_coeff))
            else:
                root_coeff_exp = list(np.random.choice(list(range(1, 4)), 2))
                root_coeff_base = int(np.random.choice(list(range(1, 20)), 1))
                coefficients[t] = root_coeff_base**Rational(min(root_coeff_exp), max(root_coeff_exp))


        exponents = [None] * terms

        for u in range(0, terms):

            if exponent_type[u]=='natural':
                exponents[u]=int(np.random.choice(list(range(0, 10)), 1, replace=False))
            elif exponent_type[u]=='negative':
                exponents[u] = int(np.random.choice(list(range(-10, -1)), 1, replace=False))
            elif exponent_type[u]=='fraction':
                frac_coeff = list(np.random.choice(list(range(1, 20)), 2))
                exponents[u] = Rational(min(frac_coeff), max(frac_coeff))

            # Root exponentials??


        expr = 0
        for i in range(0, terms):
            expr += coefficients[i] * x ** (exponents[i])

    else:
        if random() < 0.5:
            expr = Mul(polynomial(2), polynomial(2), evaluate=False)
        else:
            expr = Mul(polynomial(2), polynomial(1)**(-1), evaluate=False)

    return expr


pprint(polynomial(), use_unicode=True)

#print(integral_steps(polynomial(),x))