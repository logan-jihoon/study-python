# Try and Except test
print('How many cats do you have')
numCats = input()  # The problem occrus if a user put a string instead of numbers

try:
    if int(numCats) >= 4:
        print('That is a lot of cats')
    else: 
        print('That is not that many cats')
except ValueError:
    print('You did not enter a number')