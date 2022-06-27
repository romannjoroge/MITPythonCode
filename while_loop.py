# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# A program illustrating the concept of a while loop

# while loops are used to represent a sequence of instructions that will
# always be ran as long as a certain condition is True

# Ask the user to input whether to go left or right
n = input('You are stuck in a forest. Go right or left: ')

# Repeat the question as long as the user inputs right
while n == 'right':
    n = input('You are stuck in a forest. Go right or left: ')
    
# If the user inputs something else tell them they've escaped
print('You have escaped the forest!')