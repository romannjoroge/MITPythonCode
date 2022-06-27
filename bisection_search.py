# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 15:29:58 2022

@author: Roman
"""

# A program to find the square root of a number

# Get the number to find square root of from user
neg_flag = True
# Make sure the number is positive
while neg_flag:
    x = int(input("Number to find square root of: "))
    if x < 0:
        print("A negative number can't have a square root, provide another number!")
    else:
        break

# Create a set of possible answers using start and end values
start = 1
end = x
guess = 0
epsilon = 0.01
numGuesses = 0

while abs(guess**2 - x) >= epsilon:
       numGuesses += 1   
       print('low =', start, 'high =', end)
       # Create a set of possible answers using start and end values
       set = end + start
       
       # Guess the middle of the set
       guess = set / 2.0   
       
       if guess**2 < x:
           start = guess
       # If it is too big you change the end and repeat
       else:
           end = guess
               
print('Square root of', x, 'is', guess,
      'and it took', numGuesses, 'times to guess it')
