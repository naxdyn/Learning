# Written by Danny
# Calculates the minimum monthly payment amount needed to pay off credit in a year, 
# specifically by using bisection search to minimize runtime

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12
monthlyLower = balance / 12
monthlyHigher = (balance * (1+monthlyInterestRate)**12) / 12

minimumMonthlyPayment = (monthlyHigher+monthlyLower) / 2
remainder = balance

while abs(remainder) > 0.01:
    remainder = balance
    for i in range(12):
        monthlyUnpaidBalance = remainder - minimumMonthlyPayment
        remainder = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    if remainder < 0:    
        monthlyHigher = minimumMonthlyPayment
        minimumMonthlyPayment = (monthlyHigher+monthlyLower) / 2
    else: 
        monthlyLower = minimumMonthlyPayment
        minimumMonthlyPayment = (monthlyHigher+monthlyLower) / 2
    
print("Lowest Payment: " + str(round(minimumMonthlyPayment,2)))