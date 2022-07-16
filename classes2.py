#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 21:57:30 2022

@author: roman
"""

class Test2(object):
    def __init__(self, x):
        """
        Only allow x to be an int
        """
        assert type(x) == int, 'x should be an int'
        self.x = x
        self.changed = False
        
def testTest():
    """
    A function to test the Test2 class
    """
    # test 1 - creating a test instance with x of different types
    try:
        print('Object with x as a string:')
        obj = Test2('Hello')
        print(type(obj))
        print('Object with x as an int')
        obj = Test2(7)
        print('Object with x as a float')
        obj = Test2(3.1)
    except Exception as e:
        print('Test FAILED: Unexpected error', e)
    else:
        print('assert statement not working ?')
    finally:
        print('<----------------------------------->')
        print()
    def assertTest(x):
        """ 
        A function that can only accept an arguement of type int
        """
        assert type(x) == int, 'x should be an int'
    try:
        assertTest('Hello')
    except AssertionError:
        print('Expected assertion error')
        try:
            assertTest(7)
        except Exception as e:
            print('Unexpected Exception', e)
        else:
            print('Success')
    else:
        print('Test failed expected assertion error!')
    finally:
        print('<----------------------------------->')
        print()
        
testTest()
    