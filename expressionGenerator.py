
from sympy import *
import numpy as np
from sympy.integrals.manualintegrate import integral_steps
from sympy.integrals.manualintegrate import manualintegrate


x = symbols('x')


def polynomial(diff=2):

    if diff == 2:
        terms = int(np.random.choice(list(range(2, 5)), 1))
        coefficient_type = list(np.random.choice(['natural', 'negative', 'fraction', 'root'], terms))
        exponent_type = list(np.random.choice(['natural', 'negative', 'fraction'], terms))
    else:
        terms = 1
        coefficient_type = ['natural']
        exponent_type = ['natural']

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

    #print('alpha', coefficients)
    #print('beta', exponents)
    #print(terms)
    pprint(expr, use_unicode=True)
    return expr


polynomial()
#print(integral_steps(polynomial(),x))