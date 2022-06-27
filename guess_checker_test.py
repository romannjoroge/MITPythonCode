#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 21:00:58 2022

@author: roman
"""

def guess_calculator(high, low):
    """
    

    Parameters
    ----------
    high : int or float
        Highest possible guess
    low : int or float
        Lowest possible guess

    Returns
    -------
    int
    Guess to make that's divisible by 10

    """
    
    guess = int((high + low) / 2)
    # Makes sure that the returned geuss is divisible by 10
    if guess % 10 == 0:
        return guess
    else:
        # Makes the guess divisible by 10
        return guess - (guess % 10)
    
high = 100
low = 0
answer = 'n'

while answer != 'y':
    print('Make a guess between 0 and 100')
    guess = guess_calculator(high, low)
    
    print('Is', guess, 'the correct answer:')
    answer = input('Answer y if correct, h if high and l if low')
    # If the balance is above zero increase the monthly payement
    # Make low equal to guess and don't change high
    if answer == 'h':
        low = guess 
    elif answer == 'l':
        # If the balance is below zero decrease the monthly payement
        # Make high equal to monthly payement and don't change low 
        high = guess