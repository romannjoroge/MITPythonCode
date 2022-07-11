#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 16:54:59 2022

@author: roman
"""

def avg(grades):
    """
    Assumes that grades is a non empty list of numbers
    Returns the average of all the elements in the list
    """
    assert not len(grades) == 0, 'no grades data'
    return sum(grades) / len(grades)

