from sympy import *
import numpy as np
from fractions import Fraction as frac

x = symbols('x')

'''''
Structure.
Easiest difficulty gives sinh cosh tanh
notation a, b s.t cosh(ax + b)
'''''

def get_hyperbolics(terms = 1, version = 'simple'):
    if version == 'simple':
        hyperbolics = np.asarray(np.random.choice([sinh, cosh, tanh], terms))

    if version == 'complex':
        hyperbolics = np.asarray(np.random.choice([coth, sech, csch], terms))
    return hyperbolics


def return_hyper(difficulty = 1, version = 'simple', powers = False, fraction = False, coeff = False):
    expr = 0
    if powers == True:
        p = np.random.choice(list(range(2, 4))).item()
    else:
        p = 1
    hyperbolic = get_hyperbolics(version = version).item()

    if fraction == True:
        f = np.random.choice(list(range(1, 10)))

    else:
        f = 1

    if coeff == True:
        c = np.random.choice(list(range(2, 20)))
    else:
        c = 1

    if difficulty == 1:
        expr += c * hyperbolic(x) ** p / f

    if difficulty == 2:
        b = np.random.choice(list(range(2, 20))).item()
        expr += hyperbolic(x + b) ** p

    if difficulty == 3:
        a = np.random.choice(list(range(2, 20))).item()
        expr += hyperbolic(a*x) ** p

    if difficulty == 4:
        a = np.random.choice(list(range(2, 20))).item()
        b = np.random.choice(list(range(2, 20))).item()
        expr += hyperbolic(a*x + b)

    if difficulty == 5:
        a = np.random.choice(list(range(2, 20))).item()
        b = np.random.choice(list(range(2, 20))).item()
        expr += hyperbolic(a*x + b) ** p

    if difficulty == 6:
        a = np.random.choice(list(range(2, 20))).item()
        b = np.random.choice(list(range(2, 20))).item()
        c = np.random.choice(list(range(2, 20))).item()
        expr += (a + b*x) ** p * hyperbolic(c*x)

    if difficulty == 7:
        expr = x ** p * hyperbolic(x) ** p

    print(expr)
    return expr


for v in ['simple', 'complex']:
    for p in [False, True]:
        for d in range(1,8):
            for f in [False, True]:
                for c in [False, True]:
                    return_hyper(difficulty = d, version = v, powers = p, fraction = f, coeff = c)
