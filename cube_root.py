# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 17:07:45 2022

@author: Roman
"""

# Iterative programs

# Initialize a guess variable to zero
guess = 0
# Take a number from the user
x = int(input('Number to find cube root of: '))
while True:
    # Cube the guess
    cubed = guess ** 3
    # If guess cubed is equal to the number stop and print guess
    if cubed == x:
        print(guess)
        break
    # If guess cubed is greater than the number stop and print guess - 1
    elif cubed > x:
        print('The approximate cube root is', guess - 1)
        break
    else:
        # Else incriment guess by 1 and repeat until guess is found
        guess += 1