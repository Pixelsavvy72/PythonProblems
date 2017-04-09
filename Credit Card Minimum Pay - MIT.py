'''
Problem 1: Paying the Minimum

Write a program to calculate the credit card balance after one year if a person only pays 
the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance, 
and print to screen something of the format:

Month: 1
Minimum monthly payment: 96.0
Remaining balance: 4784.0
Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41

instead of

Remaining balance: 813.4141998135 

Finally, print out the total amount paid that year and the remaining balance at the 
end of the year in the format:

Total paid: 96.0
Remaining balance: 4784.0

A summary of the required math is found below:

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + 
(Monthly interest rate x Monthly unpaid balance)

'''

month = 1
startbal = balance
paid = 0

while month < 13:
    #1monthly payment based on prev month
    monpay = round(monthlyPaymentRate * balance, 2)
    #new balance
    newbal = round((balance - monpay) + (annualInterestRate / 12.0 * (balance-monpay)), 2)
       
    print "Month: %s" % month
    print "Minimum monthly payment: %s" % monpay
    print "Remaining balance: %s" % newbal
    
    balance = newbal
    paid = paid + monpay
    month += 1


print "Total paid: %s" % paid #NEEDS TO INCLUDE INTEREST!!!
print "Remaining balance: %s" % newbal 