# This is a pythong program for Number guess with 7 takes only

import random
# Ask a user a name & take a string value
print ('Hello. What is your name')
name = input()
# Use the taken value to generate another message
print('WEll, '+name+', I am thinking of a number between 1 and 20')

# Set a random number
secretNumber = random.randint(1,20)
print('Debug : Secreat number is ' + str(secretNumber))

# For loop to take the guess
for guessTaken in range (1,7):
    print('Take a guess')
    guess = int(input())
    if guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
    else:
        break # When you got the correct guess

if guess == secretNumber:
    print('Good job, you took ' + str(guessTaken) + ' guess.')
else:
    print('Nope. The number I was thinking of is '+ str(secretNumber) + '.')

