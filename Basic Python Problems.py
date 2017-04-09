'''
Counting Bobs

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' 
occurs in s. For example, if s = 'azcbobobegghakl', then your program 
should print

Number of times bob occurs is: 2

'''

name = 'bob'    #sets the string to search for
go = 0    #sets the starting index to 0
total = 0    #total times substring found

while go < len(s):    # continues loop until the end
    x = s.find(name, go)   # sets x to a search and startpoint
    if x > -1:    #runs while the search found bob at any index
        total = total +1    #increases the count when found
        go = x + 1    #increase the start point for the next search
    else: 
        break    #breaks when start poin is bigger than string

print total

'''
----------------------------------------------------------------------------

Counting Vowels

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5

'''

vowels = "aeiou"
total = []

def numvow(s):
    for let in vowels:
        total.append(s.count(let))
    print sum(total)
        
numvow(s)

'''
----------------------------------------------------------------------------



Problem 3: Counting and Grouping

A catering company has hired you to help with organizing and preparing customer's 
orders. You are given a list of each customer's desired items, and must write a 
program that will count the number of each items needed for the chefs to prepare. 
The items that a customer can order are: salad, hamburger, and water.

Write a function called item_order that takes as input a string named order. 
The string contains only words for the items the customer can order separated by one space. 
The function returns a string that counts the number of each item and consolidates them in the 
following order: salad:[# salad] hamburger:[# hambruger] water:[# water]

If an order does not contain an item, then the count for that item is 0. 
Notice that each item is formatted as [name of the item][a colon symbol][count of the item] 
and all item groups are separated by a space.

For example:

If order = "salad water hamburger salad hamburger" then the function returns
 "salad:2 hamburger:2 water:1"

If order = "hamburger water hamburger" then the function returns 
"salad:0 hamburger:2 water:1"


'''

def item_order(order):
    sal = order.count('salad')
    ham = order.count('hamburger')
    wat = order.count('water')


    return "salad:%s hamburger:%s water:%s" % (sal, ham, wat)

'''
----------------------------------------------------------------------------




'''