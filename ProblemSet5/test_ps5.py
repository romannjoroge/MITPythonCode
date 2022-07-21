#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:27:25 2022

@author: roman
"""
from ps5 import *

def test_dict_shift():
    # test 1 - shift is equal to zero
    answer = {'a':'a', 'b':'b', 'c':'c', 'd':'d', 'e':'e', 'f':'f', 'g':'g', 
              'h':'h', 'i':'i', 'j':'j', 'k':'k', 'l':'l', 'm':'m', 'n':'n',
              'o':'o', 'p':'p', 'q':'q', 'r':'r', 's':'s', 't':'t', 'u':'u', 
              'v':'v', 'w':'w', 'x':'x', 'y':'y', 'z':'z',
              'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G',
              'H':'H', 'I':'I', 'J':'J', 'K':'K', 'L':'L', 'M':'M', 'N':'N',
              'O':'O', 'P':'P', 'Q':'Q', 'R':'R', 'S':'S', 'T':'T', 'U':'U',
              'V':'V', 'W':'W', 'X':'X', 'Y':'Y', 'Z':'Z'}
    shift = 0
    obj = Message('hello')
    try:
        result = obj.build_shift_dict(shift)
    except Exception as e:
        print('TEST 1 FAILED! Unexpected error', e)
    else:
        if result == answer:
            print('TEST 1 SUCCESS!')
        else:
            print('TEST 1 FAILED')
    finally:
        print('<------------------------------------------>')
        
    # test 2 - shift is a small number
    shift = 3
    answer = {'a':'d', 'b':'e', 'c':'f', 'd':'g', 'e':'h', 'f':'i', 'g':'j', 
              'h':'k', 'i':'l', 'j':'m', 'k':'n', 'l':'o', 'm':'p', 'n':'q',
              'o':'r', 'p':'s', 'q':'t', 'r':'u', 's':'v', 't':'w', 'u':'x', 
              'v':'y', 'w':'z', 'x':'a', 'y':'b', 'z':'c',
              'A':'D', 'B':'E', 'C':'F', 'D':'G', 'E':'H', 'F':'I', 'G':'J',
              'H':'K', 'I':'L', 'J':'M', 'K':'N', 'L':'O', 'M':'P', 'N':'Q',
              'O':'R', 'P':'S', 'Q':'T', 'R':'U', 'S':'V', 'T':'W', 'U':'X',
              'V':'Y', 'W':'Z', 'X':'A', 'Y':'B', 'Z':'C'}
    try:
        result = obj.build_shift_dict(shift)
    except Exception as e:
        print('TEST 2 FAILED! Unexpected error', e)
    else:
        if result == answer:
            print('TEST 2 SUCCESS!')
        else:
            print('TEST 2 FAILED')
            print('Result was:', result)
            print('Answer is:', answer)
    finally:
        print('<------------------------------------------>')
        
    # test 3 shift is a large number
    shift = 100
    try:
        result = obj.build_shift_dict(shift)
    except AssertionError as e:
        print('TEST 3 SUCCESS!')
    except Exception as e:
        print('TEST 3 FAILED! Unexpected error', e)
    else:
        print('TEST 3 FAILED! Expected an assertion error!')
    finally:
        print('<------------------------------------------>')
        
    # test 4 - shift is a negative number
    shift = -1
    answer = {'a':'z', 'b':'a', 'c':'b', 'd':'c', 'e':'d', 'f':'e', 'g':'f', 
              'h':'g', 'i':'h', 'j':'i', 'k':'j', 'l':'k', 'm':'l', 'n':'m',
              'o':'n', 'p':'o', 'q':'p', 'r':'q', 's':'r', 't':'s', 'u':'t', 
              'v':'u', 'w':'v', 'x':'w', 'y':'x', 'z':'y',
              'A':'Z', 'B':'A', 'C':'B', 'D':'C', 'E':'D', 'F':'E', 'G':'F',
              'H':'G', 'I':'H', 'J':'I', 'K':'J', 'L':'K', 'M':'L', 'N':'M',
              'O':'N', 'P':'O', 'Q':'P', 'R':'Q', 'S':'R', 'T':'S', 'U':'T',
              'V':'U', 'W':'V', 'X':'W', 'Y':'X', 'Z':'Y'}
    try:
        result = obj.build_shift_dict(shift)
    except Exception as e:
        print('TEST 4 FAILED! Unexpected error', e)
    else:
        if result == answer:
            print('TEST 4 SUCCESS!')
        else:
            print('TEST 4 FAILED')
    finally:
        print('<------------------------------------------>')
        
def test_cipher():
    # test 1 - shift used is 0
    shift = 0
    text = "That one there is a violation!"
    obj = CiphertextMessage(text)
    try:
        (key, result) = obj.decrypt_message()
    except Exception as e:
        print('TEST 1 FAILED: Unexpected error', e)
    else:
        if key == shift and result == text:
            print('TEST 1 SUCCESS!')
        else:
            print('TEST 1 FAILED: Wrong key result pair')
            print('Correct key is:', shift, 'Gotten key is:', key)
            print('Correct result is:', text)
            print('Gotten text is:', result)
    finally:
        print('<------------------------------------------>')
    
    # test 2 - shift is a small number
    shift = 3
    text = "Wkdw rqh wkhuh lv d ylrodwlrq!"
    answer = "That one there is a violation!"
    obj = CiphertextMessage(text)
    try:
        (key, result) = obj.decrypt_message()
    except Exception as e:
        print('TEST 2 FAILED: Unexpected error', e)
    else:
        if key == shift and result == answer:
            print('TEST 2 SUCCESS!')
        else:
            print('TEST 2 FAILED: Wrong key result pair')
            print('Correct key is:', shift, 'Gotten key is:', key)
            print('Correct result is:', answer)
            print('Gotten text is:', result)
    finally:
        print('<------------------------------------------>')
    

test_dict_shift()
print()
print()
test_cipher()
