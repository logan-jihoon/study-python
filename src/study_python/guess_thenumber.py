# This is a test python to play a guess the number game. 

import random, sys

print ('I am thinking of a number between 1 and 20')
answer = random.randint(1,20)
count = 1

while True:
    print('Take a guess')
    guess = int(input())
    if guess == answer:
        print("Good job!, you passed my number in " + str(count) + ' guesses !')
        sys.exit()
    elif guess < answer:
        print ('Your guess is too low')
    elif guess > answer:
        print ('Your guess is too high') 
    count = count + 1
