# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# A more efficient version of fibonnaci 
def fibonacci_efficient(n, d):
    """
    

    Parameters
    ----------
    n : int
        The number to find the fibonacci of.
    d : dictionary
        Dictionar containing alreaady calculated fibonacci values.

    Returns
    -------
    Fibonacci of a number

    """
    # If the fibonacci of the number is already stored in the 
    # dictionary the value should just be returned
    if n in d:
        return d[n]
    else:
        # Calculate the fibonnacci recursively
        # Base Cases
        if n == 1 or n == 2:
            return 1
        
        # Recursive call
        ans = (fibonacci_efficient(n - 1, d) 
               + fibonacci_efficient(n - 2, d))
        # Add a new entry in the dictionary
        d[n] = ans
        return ans