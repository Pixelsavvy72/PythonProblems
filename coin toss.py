import random

count = 0
heads = 0
tails = 0
headsInARow = 0
tailsInARow = 0
most = 0
least = 0

prompt = "Enter a number > "
print "How many times would you like to flip the coin?"
times = int(raw_input(prompt))


while count < times:

    flip = random.randrange(1,3,1)
    if flip == 1:
        heads += 1
        headsInARow += 1
        tailsInARow = 0
        if headsInARow > most:
            most = headsInARow
        if least == 0:
            least = most
        if least > headsInARow:
            least = headsInARow

    else:
        tails += 1
        tailsInARow += 1 
        headsInARow = 0
        if tailsInARow > most:
            most = tailsInARow
        if least == 0:
            least = most
        if least > tailsInARow:
            least = tailsInARow

    count += 1
    
print "Heads: %s" %heads
print "Tails: %s" %tails
print "Most in a row was %s" %most
print "Least in a row was %s" %least

