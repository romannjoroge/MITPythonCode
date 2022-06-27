# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 17:14:21 2022

@author: Roman
"""

# Get a number from the user
# Number should be an integer from 0 to 99
x=int(input('Please think of a number between 0 and 100!'))
high = 100
low = 0
guess = 0
# Guess the number given by the user until it is right
while guess != x:
    # Create a possible set of answers and guess a number
    set = high + low
    guess = set // 2
    # Ask user if the guess is correct, possible answers are h,l or c
    print('Is your secret number', guess, '?')
    while True:
        ifRight = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
        if ifRight not in ['h', 'c', 'l']:
            print('Sorry, I did not understand your input.')
        else:
            break
    # If the answer is lower than the guess make end = guess
    if ifRight == 'h':
        high = guess
    # If the answer is higher than guess make start = guess
    elif ifRight == 'l':
        low = guess
    else:
        print('Game over. Your secret number was:', guess)