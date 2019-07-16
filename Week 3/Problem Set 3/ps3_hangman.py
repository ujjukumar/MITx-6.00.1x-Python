# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

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

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    m = 0
    for x in secretWord:
        if x in lettersGuessed:
            m +=1
        
        
    if len(secretWord) == m:
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    f = ''
    for x in secretWord:
        if x in lettersGuessed:
            f +=x
        
        else:
            f +='_ '
    return f

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    f = ''
    import string
    c = string.ascii_lowercase
    
    for x in c:
        if x not in lettersGuessed:
            f +=x
        else:
            f +=''
    return f
    
def hangman(secretWord):
    guessno = 8
    lettersGuessed = []
    
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ',len(secretWord) ,'letters long')
    while guessno > 0:
        if ((guessno > 0) and (not isWordGuessed(secretWord, lettersGuessed))):
            print('- - - - - - - - - - - - - - - - - - -')
            print('You have ',guessno ,'guesses left')
            print ('Available letters: ', getAvailableLetters(lettersGuessed))
            guess = input('Please guess a letter: ')
            lettersGuessed += guess
            
            if guess in secretWord:
                print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
            elif guess in getAvailableLetters(lettersGuessed):
                print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            elif guess not in secretWord:
                print("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
                guessno = guessno-1
                if guessno == 0:
                   print('Sorry, you ran out of guesses. The word was ', secretWord) 
            guess = ''
                
        elif ((guessno > 0) and (isWordGuessed(secretWord, lettersGuessed))):
            print('- - - - - - - - - - - - - - - - - - -')
            guessno = 0
            print('Congratulations, you won!')
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
