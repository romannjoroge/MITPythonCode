#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 15:57:27 2022

@author: roman
"""

from ps4a_debug import *

def isValidWordTest(wordList):
    """
    Unit Test for isValidWord
    """
    
    # test 1 wordlist is empty everything else has content
    wordList2 = []
    hand = {'e':1, 'v':1, 'n':1}
    word = 'even'
    
    try:
        isValidWord(word, hand, wordList2)
    except AssertionError:
        print('TEST 1: SUCCESS')
    except Exception as e:
        print('TEST 1: FAILURE', e)
    else:
        print('TEST 1: FAILURE AN ASSERTION ERROR WAS MEANT TO OCCUR')
    finally:
        print('---------------------------------------------')
        print()
        
    # test 2 word is empty everything else has content
    word = ''
    try:
        result = isValidWord(word, hand, wordList)
        if (result):
            print('TEST 2: FAILED RESULT WAS MEANT TO BE FALSE')
        else:
            print('TEST 2: SUCCESS')
    except Exception as e:
        print('TEST 2: FAILED', e)
    finally:
        print('---------------------------------------------')
        print()
        
    # test 3 hand is empty everything else has content
    hand = {}
    word = 'even'
    try:
        isValidWord(word, hand, wordList)
    except AssertionError:
        print('TEST 3: SUCCESS')
    except Exception as e:
        print('TEST 3: FAILURE', e)
    else:
        print('TEST 3: FAILURE AN ASSERTION ERROR WAS MEANT TO OCCUR')
    finally:
        print('---------------------------------------------')
        print()
        
    # test 4 word has letters that are missing in hand
    hand = {'e':1, 'v':1, 'n':1}
    word = 'apple'
    try:
        result = isValidWord(word, hand, wordList)
        if (result):
            print('TEST 4: FAILED RESULT WAS MEANT TO BE FALSE')
        else:
            print('TEST 4: SUCCESS')
    except Exception as e:
        print('TEST 4: FAILED', e)
    finally:
        print('---------------------------------------------')
        print()
        
    # test 5 word has letters in hand but occur more
    hand = {'e':1, 'v':1, 'n':1}
    word = 'even'
    try:
        result = isValidWord(word, hand, wordList)
        if (result):
            print('TEST 5: FAILED RESULT WAS MEANT TO BE FALSE')
        else:
            print('TEST 5: SUCCESS')
    except Exception as e:
        print('TEST 5: FAILED', e)
    finally:
        print('---------------------------------------------')
        print()
        
    # test 6 word and hand are accurate
    hand = {'e':2, 'v':1, 'n':1}
    word = 'even'
    try:
        result = isValidWord(word, hand, wordList)
        if (result):
            print('TEST 6: SUCCESS')
        else:
            print('TEST 6: FAILED RESULT WAS MEANT TO BE TRUE')
    except Exception as e:
        print('TEST 6: FAILED', e)
    finally:
        print('---------------------------------------------')
        print()
        
    # test 7 word can be made from hand but it doesn't exist
    hand = {'e':2, 'v':1, 'n':1}
    word = 'evn'
    try:
        result = isValidWord(word, hand, wordList)
        if (result):
            print('TEST 7: FAILED RESULT WAS MEANT TO BE FALSE')
        else:
            print('TEST 7: SUCCESS')
    except Exception as e:
        print('TEST 7: FAILED', e)
    finally:
        print('---------------------------------------------')
        print()
        
wordList = loadWords()
print("----------------------------------------------------------------------")
print("Testing isValidWord...")
isValidWordTest(wordList)
            
            
        
    
    
    