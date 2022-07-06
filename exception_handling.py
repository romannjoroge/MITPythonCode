#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 17:45:12 2022

@author: roman
"""

def f(x, y):
    try:
        print('Running code...')
        print(x/y)
    except ValueError:
        print('Invalid values')
    except: ZeroDivisionError() as e:
        print('Denomninator is zero!')
    except:
        print('Error Occured')
    else:
        print('Used function succesfuly')
    finally:
        print('Thanks for using function')