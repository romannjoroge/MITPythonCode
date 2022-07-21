#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 16:33:51 2022

@author: roman
"""

from hand import *

def test_hand():
    # test 1 - empty word
    word = ''
    hand = Hand(6)
    try:
        result = hand.update(word)
    except Exception as e:
        print('TEST 1 FAILED:', e)
    else:
        if result:
            print('TEST 1 SUCCESS')
        else:
            print('TEST 1 FAILED: result meant to be True')
    finally:
        print('<--------------------------------------->')
    # test 2 - empty hand
    hand = Hand(0)
    word = 'hello'
    try:
        result = hand.update(word)
    except Exception as e:
        print('Test 2 FAILED:', e)
    else:
        if (result):
            print('Test 2 FAILED! Answer meant to be False')
        else:
            print('TEST 2 SUCCESS')
    finally:
        print('<--------------------------------------->')
    # test 3 word can be made from hand
    hand = Hand(5)
    hand.setDummyHand('hello')
    try:
        result = hand.update(word)
    except Exception as e:
        print('Test 3 FAILED:', e)
    else:
        if (result):
            print('TEST 3 SUCCESS')
        else:
            print('TEST 3 FAILED: Answer meant to be True')
    finally:
        print('<--------------------------------------->')
    # test 4 - word has a letter that is not in hand
    word = 'apple'
    hand.setDummyHand('hello')
    try:
        result = hand.update(word)
    except Exception as e:
        print('TEST 4 FAILED! Unexpected error', e)
    else:
        if result:
            print('TEST 4 FAILED! Answer meant to be False')
        else:
            print('TEST 4 SUCCESS!')
    finally:
        print('<--------------------------------------->')
    # test 5 - word has too many letters
    word = 'evenon'
    hand.setDummyHand('evnon')
    try:
        hand.update(word)
    except Exception as e:
        print('TEST 5 FAILED! Unexpected error', e)
    else:
        if result:
            print('TEST 5 FAILED! Answer meant to be False')
        else:
            print('TEST 5 SUCCESS!')
    finally:
        print('<--------------------------------------->')
        
test_hand()
        