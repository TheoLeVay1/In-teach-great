from platformdirs import user_runtime_dir
from sympy import *
import numpy as np
from sympy.integrals.manualintegrate import integral_steps
from sympy.integrals.manualintegrate import manualintegrate
from fractions import Fraction as frac
import random

rng = np.random.default_rng(12345)

def has_duplicates(lst):
    mySet = set(lst)
    if len(mySet) == len(lst):
        return False
    else:
        return True

def get_fractional_powers(power_numer_range, power_denom_range, max_items=5):
    powers = []

    min_numer = power_numer_range[0]
    max_numer = power_numer_range[-1]

    min_denom = power_denom_range[0]
    max_denom = power_denom_range[-1]

    for i in range(max_items):
        power = Rational(-1,1)
        powers_temp = powers + [power]
        # no two powers can be the same
        # at least 1 power must be fractional
        # power must not be -1
        while (powers_temp[-1] == -1) or (has_duplicates(powers_temp)) or \
                (len(powers_temp) == max_items and np.all([pow.denominator == 1 for pow in powers_temp])):
            numer = np.random.randint(min_numer, max_numer+1, dtype=int)
            denom = np.random.randint(min_denom, max_denom+1, dtype=int)
            power = frac(numer, denom)
            powers_temp = powers + [power]
        powers.append(power)

    return powers

def get_powers(rng, min_power=0, max_power=5, min_terms=1):
    valid_powers = [i for i in range(min_power, max_power+1)]

    max_terms = max_power +1 - min_power
    
    mean = (max_terms + min_terms) / 2
    std = (max_terms - mean) / 3  # guarrantees over 99% of answers will be within 1 to max power

    num_terms = int(np.round(rng.normal(mean, std)))
    if num_terms < min_terms:
        num_terms = min_terms
    elif num_terms > max_terms:
        num_terms = max_terms

    powers = np.random.choice(valid_powers, num_terms, replace=False)
    powers.sort()
    return powers

def get_coefficients(terms, low=-10, high=10):
    coefficients = []
    for term in range(terms):
        coefficient = 0
        while coefficient == 0:
            coefficient = np.random.randint(low, high+1, dtype=int)
        coefficients.append(coefficient)
    return coefficients

def get_fractional_coefficients(powers, low=-10, high=10):
    '''
    coeff_numer = get_coefficients(powers)
    coeff_denom = get_coefficients(powers)

    fractional_coefficients = []
    for i in range(len(powers)):
        fractional_coefficient = frac(coeff_numer[i], coeff_denom[i])
        if fract
'''
    pass


def generate_basic_polynomial(difficulty='Hard'):
    rng = np.random.default_rng()

    match difficulty:
        case 'Easy':
            power_range = [0, 5]
            coeff_range = [-10, 10]

            powers = get_powers(rng, power_range[0], power_range[-1])

            terms = len(powers)
            coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])

        case 'Medium':
            power_range = [-5, 5]
            coeff_range = [-10, 10]

            powers = get_powers(rng, power_range[0], power_range[-1])
            terms = len(powers)

            coeff_numer = get_coefficients(terms, coeff_range[0], coeff_range[-1])
            coeff_denom = get_coefficients(terms, coeff_range[0], coeff_range[-1])

            coefficients = []
            for i in range(len(powers)):
                coefficients.append(Rational(coeff_numer[i], coeff_denom[i]))

        case 'Hard':
            coeff_range = [-10, 10]
            root_range = [1, 5]

            power_numer_range = [-5, 5]
            power_denom_range = [1, 5]

            powers = get_fractional_powers(power_numer_range, power_denom_range)
            terms = len(powers)

            coeff_base_numer = get_coefficients(terms, coeff_range[0], coeff_range[-1])
            coeff_base_denom = get_coefficients(terms, coeff_range[0], coeff_range[-1])

            coeff_root_numer = get_coefficients(terms, root_range[0], root_range[-1])
            coeff_root_denom = get_coefficients(terms, root_range[0], root_range[-1])

            coefficients = []
            #had issue where coefficient could be negative and taking negative root results in imaginary numbers
            # sorted by rooting abs value and setting sign of rooted coeff = to sign of coeff

            # WILL NOT SHOW SQRT
            for i in range(len(powers)):
                coeff_base = Rational(coeff_base_numer[i], coeff_base_denom[i])
                coeff_exp = Rational(coeff_root_numer[i], coeff_root_denom[i])

                coeff = np.sign(coeff_base) * abs(coeff_base)**coeff_exp
                coefficients.append(coeff)

    x = symbols('x')
    expr = 0
    for i in range(len(powers)):
        expr += coefficients[i] * x ** (powers[i])
    return expr

def generate_sinusoidal(difficulty='Easy', freq=1):

    x = symbols('x')
    expr = 0

    match difficulty:
        case 'Easy':
            max_terms = 2
            sinusoidals = [sin(freq*x), cos(freq*x)]
            random.shuffle(sinusoidals)
            coeff_range = [-10, 10]

            terms = np.random.randint(1,max_terms+1)  # random number either 1 or 2
            coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])
    
    for i in range(terms):
        expr += coefficients[i] * sinusoidals[i]
    return expr

def generate_exponential_euler(freq=1):

    x = symbols('x')
    expr = 0

    terms = 1
    coeff_range = [-10, 10]
    coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])

    for i in range(terms):
        expr += coefficients[i] * exp(x)
    return expr

def generate_exponential(freq=1):

    x = symbols('x')
    expr = 0

    terms = 1
    coeff_range = [2, 10]
    coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])

    for i in range(terms):
        expr += coefficients[i] ** (freq*x)
    return expr

def generate_log_differential():
    
    x = symbols('x')
    expr = 0
    
    terms = 1
    coeff_range = [-10, 10]
    coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])

    for i in range(terms):
        expr += coefficients[i] / x
    return expr

def generate_polynomial_substitution(difficulty='Hard'):

    x = symbols('x')
    expr = 0

    terms = 2
    coeff_range = [-10, 10]
    coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])

    P = np.random.randint(3, 9)

    match difficulty:
        case 'Easy':
            N = np.random.randint(1, 6)
            expr1 = N*coefficients[0]* x**(N-1)
            expr2 = coefficients[0]* x**N + coefficients[1]

            expr = expr1 * expr2 **P
        case 'Medium':
            R = 0
            N = np.random.randint(1, 6)
            expr1 = N*coefficients[0]* x**(N-1)
            expr2 = coefficients[0]* x**N + coefficients[1]
            
            while R == 0 or R == 1:
                R = np.randint(-4, 5)
            expr = R * expr1 * expr2 **P
        case 'Hard':
            rng = np.random.default_rng()
            N1, N2 = 0, 0
            while N1 == N2:
                N1 = np.random.randint(-2, 3)
                N2 = np.random.randint(-2, 3)
            R = 0
            while R == 0 or R == 1:
                R = np.random.randint(-4, 5)

            expr1 = N1*coefficients[0] * x**(N1-1) + N2* coefficients[1]* x**(N2-1)
            expr2 = coefficients[0] * x**N1 + coefficients[1]* x**N2

            expr = R * expr1 * expr2 **P

    return expr

def generate_exp_polynomial(difficulty='Medium'):

    x = symbols('x')
    expr = 0

    terms = 2
    coeff_range = [-10, 10]
    coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])
    A1 = coefficients[0]
    A2 = coefficients[1]

    match difficulty:
        case 'Easy':
            N = np.random.randint(1, 6)
            expr1 = exp(A1 * x**N + A2)
            expr2 = N* A1 * x**(N-1)

            expr = expr1 * expr2
        case 'Medium':
            N = np.random.randint(1, 6)
            R = 0
            while R == 0:
                R = np.random.randint(-5, 5)
            expr1 = exp(A1 * x**N + A2)
            expr2 = R* N * A1 * x**(N-1)

            expr = expr1 * expr2
        case 'Hard':
            N1 = np.random.randint(-2, 2)
            N2 = np.random.randint(-2, 2)
            R = 0
            while R == 0:
                R = np.random.randint(-5, 5)
            expr1 = exp(A1 * x**N1 + A2* x**N2)
            expr2 = R*N1*A1*x**(N1-1) + N2*A2*x**(N2-1)

            expr = expr1 * expr2

    return expr 

def generate_log_polynomial(difficulty='Hard'):

    x = symbols('x')
    expr = 0

    terms = 2
    coeff_range = [-10, 10]
    coefficients = get_coefficients(terms, coeff_range[0], coeff_range[-1])
    A1 = coefficients[0]
    A2 = coefficients[1]

    match difficulty:
        case 'Easy':
            N = np.random.randint(1,5)

            expr1 = N*A1*x**(N-1)
            expr2 = A1*x**N + A2
            expr = expr1 / expr2
        case 'Medium':
            N = np.random.randint(1,5)
            R = 0
            while R==0:
                R = np.random.randint(-5, 6)

            expr1 = R*N*A1*x**(N-1)
            expr2 = A1*x**N + A2
            expr = expr1 / expr2
        case 'Hard':
            N1 = np.random.randint(-2, 2)
            N2 = np.random.randint(-2, 2)
            R = 0
            while R == 0:
                R = np.random.randint(-5, 5)

            expr1 = R*N1*A1*x**(N1-1) + N2*A2*x**(N2-1)
            expr2 = A1*x**N1 + A2*x**N2
            expr = expr1 / expr2
    
    return expr

log_polynomial = generate_log_polynomial()
pprint(log_polynomial, use_unicode=True)

exp_polynomial = generate_exp_polynomial()
pprint(exp_polynomial, use_unicode=True)

poly_subst = generate_polynomial_substitution()
pprint(poly_subst, use_unicode=True)

log_differential = generate_log_differential()
pprint(log_differential, use_unicode=True)

exponential = generate_exponential()
pprint(exponential, use_unicode=True)

exponential_eul = generate_exponential_euler()
pprint(exponential_eul, use_unicode=True)

sinusoidal = generate_sinusoidal()
pprint(sinusoidal, use_unicode=True)

polynomial = generate_basic_polynomial('Hard')
pprint(polynomial, use_unicode=True)

nums =[]
for i in range(1000):
    num = int(np.round(rng.chisquare(3.5)))
    nums.append(num)

for i in range(6):
    print(f'Count of {i} in nums is : {nums.count(i)}')

#Count of 1 in nums is : 520
#Count of 2 in nums is : 280
#Count of 3 in nums is : 90
#Count of 4 in nums is : 47
#Count of 5 in nums is : 63