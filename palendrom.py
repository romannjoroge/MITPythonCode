#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:30:58 2022

@author: roman
"""

def palendrom(x):
    if len(x) <= 1:
        return True
    else:
        return x[0] == x[-1] and palendrom(x[1:-1])