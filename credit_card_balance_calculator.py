#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:54:45 2022

@author: roman
"""

# Program to calculate the remaining balance in a credit card after a year

# Accept the current unpaid balance, a monthly minimum payement percentage
# and an annual interest rate
def balance_calculator(balance, annualInterestRate, monthlyPaymentRate):
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
    
    # Calculate the amount paid
    amount_paid = balance * monthlyPaymentRate
    
    # Calculate the new unpaid balance without interest
    unpaid_balance = balance - amount_paid
    
    # Calculate new unpaid balance with interest
    unpaid_balance = unpaid_balance + (unpaid_balance * 
                                       (annualInterestRate / 12))
    return unpaid_balance

# Values to be used in the balance_calculator function
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

# Counting the balance after 1 year
num_months = 1
while num_months < 13:
    balance = balance_calculator(balance, annualInterestRate, 
                                 monthlyPaymentRate);
    print('Month', num_months, 'Remaining balance:', balance)
    num_months += 1
    
print('Remaining balance:', round(balance, 2))