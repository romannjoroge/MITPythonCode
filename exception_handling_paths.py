#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:58:49 2022

@author: roman
"""

def raise_2nd_exception():
    try:
        pass
        print('I am in the try block')
        # raise IndexError  # will be a handled exception
        # raise ZeroDivisionError  # unhandled exception
    except IndexError:
        print('I am in the except block')
        pass
        raise Exception("Exception in except IE")
    else:
        print('I am in the else block')
        pass
        raise Exception("Exception in else")
    finally:
        print("***### Finally ###***")
        print("then it will reraise unhandled or 2nd exception unless there is")
        print("an exception in the finally clause\n")
        raise Exception("See what happens if there is an exception in finally")
        
raise_2nd_exception()