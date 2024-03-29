'''
Problem 4 - The Game
6.0/15.0 points (graded)
Now you will implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.

Hints:
You should start by noticing where we're using the provided functions (at the top of ps3_hangman.py) to load the words and pick a random one. Note that the functions loadWords and chooseWord should only be used on your local machine, not in the tutor. When you enter in your solution in the tutor, you only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message telling them they've already guessed that - so try again!).
Sample Output
The output of a winning game should look like this...
And the output of a losing game should look like this...

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, or getAvailableLetters, you do not need to paste your definitions in the box. We have supplied our implementations of these functions for your use in this part of the problem. If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to input to get the user's guess.
'''


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
    intro = str(len(secretWord))
    lettersGuessed = []
    guess = str
    mistakesMade = 8
    wordGuessed = False
    
    print 'Welcome to the game, Hangman!'
    print ('I am thinking of a word that is ') + intro + (' letters long.')
    print ('------------')

    while mistakesMade > 0 and mistakesMade <= 8 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ('You have ') + str(mistakesMade) + (' guesses left.')
        print ('Available letters: ') + getAvailableLetters(lettersGuessed)
        guess = raw_input('Please guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ('Good guess: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Oops! You've already guessed that letter: ") + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakesMade -= 1
                print ('Oops! That letter is not in my word: ') + getGuessedWord(secretWord, lettersGuessed)
                print ('------------')

    if wordGuessed == True:
        return 'Congratulations, you won!'
    elif mistakesMade == 0:
        print ('Sorry, you ran out of guesses. The word was ') + secretWord