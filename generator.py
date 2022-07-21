#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 18:30:56 2022

@author: roman
"""

def genPrimes():
    """
    A function that generates a list of prime numbers
    """
    prime = [2]
    number = 3
    while True:
        isPrime = True
        for num in prime:
            if number % num == 0:
                isPrime = False
        if isPrime:
            prime.append(number)
            yield number
        number += 1
        
primes = genPrimes()