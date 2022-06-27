# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cmath
def is_even(i):
    """

    Parameters
    ----------
    i : TYPE integer
        DESCRIPTION:
            The number you want to find whether its even or not

    Returns
    -------
    Boolean

    """
    return i % 2 == 0

print(is_even(3))


def square_root(a):
    """
    a : int or float
    RETURN an int or float
    """
    guess = 0
    epsilon = 0.01
    high = abs(a)
    low = 0
    # Repeat until the guess^2 is approximate to a
    while abs(guess ** 2 - a) > epsilon:
        # Create a set of possible answers
        set = high + low
        # Get a guess from the set
        guess = set / 2.0
        # If the guess is to high make guess high in set
        if guess**2 > a:
            high = guess
            print(guess, "is too high!")
        # If the guess is to low make guess low in set
        if guess **2 < a:
            low = guess
            print(guess, "is too low")
    return guess
    
    
def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    c = c - x
    numerator = -b - square_root((b**2 - 4*a*c))
    denominator = 2 * a
    return numerator / denominator

print(evalQuadratic(1, 0, 4, 4))


