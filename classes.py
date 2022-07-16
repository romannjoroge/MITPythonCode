#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 20:33:54 2022

@author: roman
"""
# Make sure to use keyword class when defining a class
class Test(object):
    """
    A Test class that will have a x value that's an int
    You can print objects of the class, add them and modify x
    """
    def __init__(self, x):
        """
        Assumes x is an int
        """
        assert type(x) == int, 'x should be an int'
        self.x = x
        self.modified = False
    def __str__(self):
        """
        Returns the string to print
        """
        return '< ' + str(self.x) + ' >'
    def __add__(self, other):
        """ 
        Assumes that other is an instance of Test
        """
        assert isinstance(other, Test) == True, 'Object of type Test should be provided as an argument'
        return Test(self.x + other.x)
    def random(self):
        print('LOL LMAO this is a random function')

# Tests on Test
def testTest():
    """ 
    A function for testing features of test
    """
    # test 1 - can you create a Test object with no x value
    try:
        obj = Test()
        print(obj)
    except Exception as e:
        print('Test 1 FAILED: Unexpected error',e)
    else:
        print('Test 1 : You can create an instance without x')
    finally:
        print('<------------------------------------------------->')
        print()
    # test 2 - create a Test object with an x that isn't an int
    try:
        obj = Test('7')
        print(obj)
    except AssertionError:
        print('Test 2 SUCCESS')
    except Exception as e:
        print('Test 2 FAILED Unexpected error', e)
    else:
        print('Test 2 FAILED an assertion error was meant to be generated')
    finally:
        print('<------------------------------------------------->')
        print()
    # test 3 - printing self
    obj = Test(4)
    try:
        print('Test 3: printing instance')
        print(obj)
    except Exception as e:
        print('Test 3 FAILED: Unexpected error', e)
    finally:
        print('<------------------------------------------------->')
        print()
    # test 4 - adding an int to a Test object
    try:
        print(obj + 4)
    except AssertionError:
        print('Test 4 SUCCESS: produced an assertion error')
    except Exception as e:
        print('Test 4 FAILED: Unexpected error', e)
    else:
        print('Test 4 FAILED: AssertionError expected')
    finally:
        print('<------------------------------------------------->')
        print()
    # test 5 - adding a Test object
    try:
        obj2 = obj + Test(5)
        print(obj2)
    except Exception as e:
        print('Test 5 FAILED: Unexpected error', e)
    else:
        print('Test 5 SUCCESS')
    finally:
        print('<------------------------------------------------->')
        print()
    # test 6 - testing random
    try:
        obj.random()
    except Exception as e:
        print('Test 6 FAILED: Unexpected error', e)
    else:
        print('Test 6 SUCCESS')
    finally:
        print('<------------------------------------------------->')
        print()
    
testTest()