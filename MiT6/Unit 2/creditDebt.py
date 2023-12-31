# Written by Danny
# Calculates the remaining balance after 1 year of minimum monthly payments

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = annualInterestRate / 12

for i in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance + (monthlyInterestRate*monthlyUnpaidBalance)

print("Remaining balance: " + str(round(balance, 2)))

