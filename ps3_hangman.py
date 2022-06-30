# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def getLetters(s):
    """
    From a string s it returns a list of all the unique letters
    """
    # Create an empty list to store the unique letters
    letters = []
    for letter in s:
        if letter not in letters:
            letters.append(letter)
    return letters
    


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # Get a list of the letters in secretWord
    letters = getLetters(secretWord)
    
    # Check if there is a letter in letters that isn't in lettersGuessed
    for letter in letters:
        if letter not in lettersGuessed:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # Lists containing the filled word with blanks for missing letters and a 
    # list of correctly guessed words
    filled_list = []
    correct = []
    
    # Goes through secretWord
    for letter in secretWord:
        # Searches for the letter in correct then lettersGuessed
        if letter in correct or letter in lettersGuessed:
            # Adds the letter to the list if in either correct or lettersGuessed
            filled_list.append(letter)
        else:
            # Adds a space and underscore if the letter in secretWord isn't in 
            # lettersGuessed
            filled_list.append('_ ')
    
    # Returns string version of filled_list
    return ''.join(str(char) for char in filled_list)




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # List of available letters
    available_list = []
    
    # Compare every character in alphabet to lettersGuessed
    for char in string.ascii_lowercase:
        # If char is not in lettersGuessed or char is less than the char add char
        # to list of available letters
        if char not in lettersGuessed:
            available_list.append(char)
    
    # Return list version of available list
    return ''.join(str(char) for char in available_list)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    num_guesses = 0
    lettersGuessed = []
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secretWord), 'letters long.')
    print('----------')
           
    
    # Repeats as long as less than 9 guesses have been made and the word isn't
    # guessed
    while num_guesses < 8 and not isWordGuessed(secretWord, lettersGuessed):
        print('You have', 8 - num_guesses, 'guesses left.')
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",
                       getGuessedWord(secretWord, lettersGuessed))
        else:
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Oops! That letter is not in my word:', 
                      getGuessedWord(secretWord, lettersGuessed))
                num_guesses += 1
            elif guess in lettersGuessed:
                print("Oops! You've already guessed that letter:",
                       getGuessedWord(secretWord, lettersGuessed))
            
        print('------------')
        
    if num_guesses > 7:
        print('Sorry, you ran out of guesses. The word was', secretWord)
    else:
        print('Congratulations, you won!')
        
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
