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
    '''''
    FUNCTION: returns expression

    Difficulty defines complexity

    General variables applied to all difficulties
    version - 'simple', 'complex' --> [sinh, cosh, tanh], [coth, sech, csch]
    powers - True takes hyperbolic to the power
    fraction - True makes hyperbolic a random (range confined) fraction
    coeff - True adds random (range confined) coefficient

    '''''
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
        # OUTPUTS e.g. cosh(x), cosh^2(x), 1/3cosh^2(x)
        expr += c * hyperbolic(x) ** p / f

    if difficulty == 2:
        # OUTPUTS e.g. 3sinh(x + 4), sinh(x + 4)
        b = np.random.choice(list(range(2, 20))).item()
        expr += c * hyperbolic(x + b) ** p

    if difficulty == 3:
        # OUTPUTS e.g. 4coth(3x)^3
        a = np.random.choice(list(range(2, 20))).item()
        expr += c * hyperbolic(a*x) ** p

    if difficulty == 4:
        # OUTPUTS e.g. 2csch(2x + 6)
        a = np.random.choice(list(range(2, 20))).item()
        b = np.random.choice(list(range(2, 20))).item()
        expr += c * hyperbolic(a*x + b) ** p

    if difficulty == 5:
        # OUTPUTS e.g. 3xsinh(x)
        expr = c * x ** p * hyperbolic(x) ** p

    if difficulty == 6:
        # OUTPUTS e.g. (4 + 3x)^2tanh^2
        a = np.random.choice(list(range(2, 20))).item()
        b = np.random.choice(list(range(2, 20))).item()
        c = np.random.choice(list(range(2, 20))).item()
        expr += c * (a + b*x) ** p * hyperbolic(c*x)

    if difficulty == 6:
        # OUTPUTS e.g. 3xsinh(x)
        expr = c * x ** p * hyperbolic(x) ** p

    print(Integral(expr))
    return expr

for v in ['simple', 'complex']:
    for p in [False, True]:
        for d in range(1,7):
            for f in [False, True]:
                for c in [False, True]:
                    return_hyper(difficulty = d, version = v, powers = p, fraction = f, coeff = c)
