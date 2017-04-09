'''
Part 1: Is the word guessed?

We'll start by writing 3 simple functions that will help us easily code the 
Hangman problem. First, implement the function isWordGuessed that takes in two 
parameters - a string, secretWord, and a list of letters, lettersGuessed. This 
function returns a boolean - True if secretWord has been 
guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print isWordGuessed(secretWord, lettersGuessed)
False
For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.

'''

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    word = list(secretWord)

    for item in word:
        if item not in lettersGuessed:
            return False
    return True

'''
-----------------------------------------------------------------------------------------


Part 2: Printing Out the User's Guess

Next, implement the function getGuessedWord that takes in two 
parameters - a string, secretWord, and a list of letters, lettersGuessed. This 
function returns a string that is comprised of letters and underscores, based on what
letters in lettersGuessed are in secretWord. This shouldn't be too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getGuessedWord(secretWord, lettersGuessed)
'_ pp_ e'

When inserting underscores into your string, it's a good idea to add at least a 
space after each one, so it's clear to the user how many unguessed letters are 
left in the string (compare the readability of ____ with _ _ _ _ ). This is called 
usability - it's very important, when programming, to consider the usability of 
your program. If users find your program difficult to understand or operate, they won't use it!

For this function, you may assume that all the letters in secretWord and lettersGuessed 
are lowercase.

'''

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = list(secretWord)

    count = 0
    ins = "_ "
    for item in word:
        if item not in lettersGuessed:
            word.pop(count)
            word.insert(count, ins)
        count += 1
    word = ''.join(word)
    return word
            

'''
-----------------------------------------------------------------------------------------

Part 3: Printing Out all Available Letters

Next, implement the function getAvailableLetters that takes in one 
parameter - a list of letters, lettersGuessed. This function returns a string 
that is comprised of lowercase English letters - all lowercase English letters 
that are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print getAvailableLetters(lettersGuessed)
abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, as 
in the example above.

For this function, you may assume that all the letters in lettersGuessed are lowercase.

Hint: You might consider using string.ascii_lowercase, which is a string comprised 
of all lowercase letters:

>>> import string
>>> print string.ascii_lowercase
abcdefghijklmnopqrstuvwxyz

'''

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alpha = list(string.ascii_lowercase)
    newalpha = []
    
    for item in alpha:
        if item not in lettersGuessed:
            newalpha.append(item)
    newalpha = ''.join(newalpha)
    return newalpha


'''
-----------------------------------------------------------------------------------------

Part 4: The Game/Complex Tests

Now you will implement the function hangman, which takes one parameter - the 
secretWord the user is to guess. This starts up an interactive game of Hangman 
between the user and the computer. Be sure you take advantage of the three helper 
functions, isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined 
in the previous part.

Hints:
You should start by noticing where we're using the provided functions 
(at the top of ps3_hangman.py) to load the words and pick a random one. 
Note that the functions loadWords and chooseWord should only be used on your local 
machine, not in the tutor. When you enter in your solution in the tutor, you 
only need to give your hangman function.

Consider using lower() to convert user input to lower case. For example:

guess = 'A'
guessInLowerCase = guess.lower()
Consider writing additional helper functions if you need them!

There are four important pieces of information you may wish to store:

secretWord: The word to guess.
lettersGuessed: The letters that have been guessed so far.
mistakesMade: The number of incorrect guesses made so far.
availableLetters: The letters that may still be guessed. Every time a player 
guesses a letter, the guessed letter must be removed from availableLetters (and if 
they guess a letter that is not in availableLetters, you should print a message telling 
them they've already guessed that - so try again!).

Note that if you choose to use the helper functions isWordGuessed, getGuessedWord, 
or getAvailableLetters, you do not need to paste your definitions in the box. We have 
supplied our implementations of these functions for your use in this part of the problem. 
If you use additional helper functions, you will need to paste those definitions here.

Your function should include calls to raw_input to get the user's guess.

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
    # FILL IN YOUR CODE HERE...
    remain = 8 
    lettersGuessed = []  
    word = list(secretWord) 
    end = [] 
      
      
    print "Welcome to the game, Hangman!" 
    print "I am thinking of a word that is %s letters long." % len(secretWord) 
          
    while True: 
        print "-------------" 
           
             
        print "You have %s guesses left." % remain 
        print "Available letters: %s" % (getAvailableLetters(lettersGuessed))  
        guess = raw_input("Please guess a letter: ") 
        guess = guess.lower() 
        lettersGuessed.append(guess) 
        ans = set(word).intersection(lettersGuessed) 
          
        if isWordGuessed(secretWord, lettersGuessed) == True: 
            print "Good guess: %s" % (getGuessedWord(secretWord, lettersGuessed))
            print "-------------" 
            print "Congratulations, you won!" 
            break 
        elif guess in secretWord and guess not in end: 
            print "Good guess: %s" % (getGuessedWord(secretWord, lettersGuessed)) 
        elif guess in end: 
            print "Oops! You've already guessed that letter: %s" % (getGuessedWord(secretWord, lettersGuessed)) 
        elif guess not in secretWord and guess not in end: 
            remain -= 1 
            print "Oops! That letter is not in my word: %s" % (getGuessedWord(secretWord, lettersGuessed)) 
            if remain == 0: 
                word = ''.join(word) 
                print "-------------" 
                print "Sorry, you ran out of guesses. The word was %s." % word 
                break 
          
          
        end.append(guess) 
