#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 13:52:59 2022

@author: roman
"""

def balance_end_year(balance, annualInterestRate, monthlyPayment):
    """
    

    Parameters
    ----------
    balance : int or float
        Balance at beggining of the year
    annualInterestRate : float
        Annual interest rate on the balance
    monthyPayement : int or float
        Fixed monthly payement at the end of every month

    Returns
    -------
    The balance at the end of the year

    """
    
    def balance_calculator(balance, annualInterestRate, monthlyPayment):
      """
      

      Parameters
      ----------
      balance : int or float
          The balance in card before monthly payement
      annualInterestRate : int or float
          The percentage annual interest on the balance
      monthlyPaymentRate : TYPE
          The minimum percentage of unpaid debt to pay back every month.

      Returns
      -------
      int or float
      The new credit balance at the end of the month

      """
      unpaid_balance = balance - monthlyPayment
      interest = unpaid_balance * (annualInterestRate / 12)
      new_balance = unpaid_balance + interest
      return new_balance
    
    new_balance = balance
    i = 0
    while i < 12:
        new_balance = balance_calculator(new_balance, annualInterestRate
                                         , monthlyPayment)
        i += 1
    return new_balance

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

balance = 891
annualInterestRate = 0.18

# Make a guess using guess_calculator
high = balance
low = 0
guess = 0

new_balance = balance
# Repeat guessing until new_balance is < 0
while new_balance > 0:
    # Create a guess monthly payment
    # guess = guess_calculator(high, low)
    
    # Calculate the balance with the guess
    new_balance = balance_end_year(balance, annualInterestRate, guess)
    
    if new_balance > 0:
        guess += 10
   

print('Lowest Payment:', guess)

