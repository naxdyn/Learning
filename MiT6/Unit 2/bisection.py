# Guesses the number input by the user using Bisection Search
# Written by Danny

high = 100
low = 0
guess = (high + low) / 2


print("Please think of a number between 0 and 100!")

while guess >= low and guess <= high:
    print("Is your secret number " + str(guess) + "?")
    answer = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if answer == 'h':
        high = guess
        guess = (high + low) // 2
    elif answer == 'l':
        low = guess
        guess = (high + low) // 2
    elif answer == 'c':
        break
    else: 
        print("Sorry, I did not understand your input.")
print("Game over. Your secret number was: " + str(guess))
