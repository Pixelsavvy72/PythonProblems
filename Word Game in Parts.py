'''
 This game is a lot like Scrabble or Words With Friends, if you've played those. 
 Letters are dealt to players, who then construct one or more words out of their 
 letters. Each valid word receives a score, based on the length of the word and 
 the letters in that word.

The rules of the game are as follows:

Dealing
A player is dealt a hand of n letters chosen at random (assume n=7 for now).

The player arranges the hand into as many words as they want out of the letters, 
using each letter at most once.

Some letters may remain unused (these won't be scored).

Scoring
The score for the hand is the sum of the scores for each word formed.

The score for a word is the sum of the points for letters in the word, multiplied 
by the length of the word, plus 50 points if all n letters are used on the first 
word created.

Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is worth 3, 
D is worth 2, E is worth 1, and so on. 
We have defined the dictionary SCRABBLE_LETTER_VALUES that maps each 
lowercase letter to its Scrabble letter value.

For example, 'weed' would be worth 32 points ((4+1+1+2) for the four letters, 
then multiply by len('weed') to get (4+1+1+2)*4 = 32). Be sure to check that 
the hand actually has 1 'w', 2 'e's, and 1 'd' before scoring the word!

As another example, if n=7 and you make the word 'waybill' on the first try, 
it would be worth 155 points (the base score for 'waybill' is (4+1+4+3+1+1+1)*7=105, 
plus an additional 50 point bonus for using all n letters).

_________________________________________________________________________________

PART 1: Get Word Score:

'''
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    count = 0  #Need to add bonus points and multiply for word score
    letValue = 0
    
    for let in word:  # assigns value to letter and increases count
        letValue += SCRABBLE_LETTER_VALUES[let]
        count += 1
    
    letValue *= count #multiplies value of the letters by length of word
    
    if count == n: # Adds 50 points if all letters used
        letValue += 50
        
    return letValue

'''
_________________________________________________________________________________

Part 2: Update Hand

'''

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    newHand = hand.copy()
    for let in word:
        if let in newHand:
            newHand[let] -= 1
    
    return newHand   

'''
_________________________________________________________________________________

Part 3: Check Validity of Words

'''

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handCheck = hand.copy()
    letters = 0
    inFiles = 0
    
    if word in wordList:
        inFiles += 1
    for let in word:
        if let in handCheck and handCheck[let] > 0:
            handCheck[let] -= 1
            letters += 1
        else:
            pass
    if letters == len(word) and inFiles == 1:
        return True        
    else:
        return False

'''
_________________________________________________________________________________

Part 4: Get Hand Length Helper Function

'''

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    return sum(hand.values())

'''
_________________________________________________________________________________

Part 5: Play Hand

'''

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # Keep track of the total score
    total = 0
    # As long as there are still letters left in the hand:
    while True:
        while calculateHandlen(hand) > 0: 
            # Display the hand
            print "Current Hand: ", 
            displayHand(hand)
            # Ask user for input
            word = raw_input("Enter word, or a \".\" to indicate that you are finished: ")
            # If the input is a single period:
            if word == ".":
                # End the game (break out of the loop)
                break
            
            # Otherwise (the input is not a single period):
            else:
                # If the word is not valid:
                if isValidWord(word, hand, wordList) == False:
                    # Reject invalid word (print a message followed by a blank line)
                    print "Invalid word, please try again."
                    
                # Otherwise (the word is valid):
                else:
                    # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                    print "\"%s\" earned %s points. Total: %s points" % (word, getWordScore(word, n), total + getWordScore(word, n))
                    total = total + getWordScore(word, n)
                    # Update the hand 
                    hand = updateHand(hand, word)
                    #old hand = updateHand(hand, word)
                
                
                
                

        # Game is over (user entered a '.' or ran out of letters), so tell user the total score
        if word == '.':
            print "Goodbye! Total score: %s points." % total
            break
    
        else:
            print "Ran out of letters. Total score: %s points." % total
            break
        
'''
_________________________________________________________________________________

Part 6: Play a Game

'''

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    n = HAND_SIZE

      
                
    # Counts played games to make sure at least one game has been played for 'r'.
    played = 0
    while True:
    
    # Asks the user to input 'n' or 'r' or 'e'.
        newGame = raw_input(" Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
      
          
    # If the user inputs 'n', let the user play a new (random) hand.
        if newGame == 'n':
        
        
            hand = dealHand(n)
            playHand(hand, wordList, n)
            played += 1
  
        
    # If the user inputs 'r', let the user play the last hand again.
        elif newGame == 'r':
            if played == 0:
                print"You have not played a hand yet. Please play a new hand first!"
            else:
                playHand(hand, wordList, n)
                 

       

    # If the user inputs 'e', exit the game.
        elif newGame == 'e':
            return 
    # If the user inputs anything else, tell them their input was invalid.
        else:
            print "Invalid command."

'''
_________________________________________________________________________________

Part 7: Computer Chooses a Word

'''

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        if isValidWord(word, hand, wordList) == True:
            # Find out how much making that word is worth
            wordScore = getWordScore(word, n) #Do I need a variable?
            # If the score for that word is higher than your best score
            if wordScore > maxScore:
                # Update your best score, and best word accordingly
                maxScore = wordScore
                bestWord = word

    # return the best word you found.
    return bestWord

'''
_________________________________________________________________________________

Part 8: Computer Plays a Hand

'''


def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    total = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0: 
        # Display the hand
        print "Current Hand: ", 
        displayHand(hand)
        # Computer chooses a word
        word = compChooseWord(hand, wordList, n)
        # If there are no more words available:
        if compChooseWord(hand, wordList, n) == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else:
            # If the word is not valid:
            if isValidWord(word, hand, wordList) == False:
                # Reject invalid word (print a message followed by a blank line)
                print "Invalid word, please try again."
                
            # Otherwise (the word is valid):
            else:
                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print "\"%s\" earned %s points. Total: %s points" % (word, getWordScore(word, n), total + getWordScore(word, n))
                total = total + getWordScore(word, n)
                # Update the hand 
                hand = updateHand(hand, word)
    print "Total score: %s points." % total
                
'''
_________________________________________________________________________________

Part 9: You and Your Computer

'''

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
          But if no hand was played, output "You have not played a hand yet. 
          Please play a new hand first!"
        
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    #deal = dealHand(n)
    #hand = deal 
      
                
    # Counts played games to make sure at least one game has been played for 'r'.
    played = 0
    
    
    # Asks the user to input 'n' or 'r' or 'e'.
    #newGame = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        
          
    # If the user inputs 'n', let the user play a new (random) hand.
    while True:
         # Asks the user to input 'n' or 'r' or 'e'.
        newGame = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if newGame == 'n':
            hand = dealHand(n)
            while True:
                whoPlays = raw_input("Enter u to have yourself play, c to have the computer play: ")
            
                
                if whoPlays == 'u':
                    playHand(hand, wordList, n)
                    break
                elif whoPlays == 'c':
                    compPlayHand(hand, wordList, n)
                    break
                else:
                    print "Invalid command."
                    continue
            played += 1        
            continue            
                   
    # If the user inputs 'r', let the user play the last hand again.
        
        if newGame == 'r' and played == 0:
            print"You have not played a hand yet. Please play a new hand first!"
            continue
        elif newGame == 'r' and played > 0:       
            while True:    
                whoPlays = raw_input("Enter u to have yourself play, c to have the computer play: ")
                if played > 0 and whoPlays == 'u':
                    playHand(hand, wordList, n)
                    break
                elif played > 0 and whoPlays == 'c':
                    compPlayHand(hand, wordList, n)
                    break
                else:
                    print "Invalid command." 
                    break
        
            continue
       

        # If the user inputs 'e', exit the game.
        if newGame == 'e':
            return 
        # If the user inputs anything else, tell them their input was invalid.
        else:
            print "Invalid command."
      
            
        
   
            