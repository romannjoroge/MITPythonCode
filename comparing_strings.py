# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 22:30:10 2022

@author: Roman
"""

# Program to emulate string comparisons

# Get 2 strings from the user
a = input('String 1: ')
b = input('String 2: ')
# Return the largest string and print it
# Find the length of the shorter of the 2 strings
len1 = len(a)
len2 = len(b)
# Get the length of string 1 and compare to string 2
if len1 < len2:
    shortest = len1
else:
    shortest = len2
    
smallest = None
# Compare ASCII code of characters in same position of the 2 strings N times
for i in range(shortest):
    # If the characters are the same move to the next character
    if ord(a[i]) == ord(b[i]):
        continue
    # If not compare the 2 characters
    else:
        # The lower character belongs to the smaller string
        if ord(a[i]) < ord(b[i]):
            smallest = a
        else:
            smallest = b  # Return the smallest
            
# If all characters are the same say that the strings are equal
if smallest == None:
    print('Both strings are equal')