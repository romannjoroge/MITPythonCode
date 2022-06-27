#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 19:03:32 2022

@author: roman
"""

import math

def polysum(n, s):
    """
    n: int that represents the number of sides in the 
       polygon
    s: int or float that represents the length of each
       side of the polygon
    
    RETURNS sum of area and square of the perimeter of the
    polygon
    """
    
    def square_perimeter(n, s):
        """
        RETURNS squared perimeter of polygon
        """
        perimeter = n * s
        return perimeter ** 2
    
    def area(n, s):
        """
        RETURNS the area of the polygon
        """
        numerator = 0.25 * n * (s ** 2)
        denominator = math.tan(math.pi / n)
        return numerator / denominator
    
    pol_area = area(n, s)
    pol_sqperim = square_perimeter(n, s)
    return round(pol_area + pol_sqperim, 4)