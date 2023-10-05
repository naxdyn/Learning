# Written by Danny
# Calculates the minimum monthly payment amount needed to pay off credit in a year

balance = 3926
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12
minimumMonthlyPayment = 10

while balance > 0:
    counter = balance
    for i in range(12):
        monthlyUnpaidBalance = counter - minimumMonthlyPayment
        counter = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)
    if counter < 0:    
        balance = counter
    else: 
        minimumMonthlyPayment = minimumMonthlyPayment + 10
    
print("Lowest Payment: " + str(minimumMonthlyPayment))
