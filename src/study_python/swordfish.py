# this is a test program for continue statement in the while loop.

while True:
    print ('what is your name?')
    name = input()
    if name != 'Joe':
        continue
    print('what is your password? (it is a fish)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')


# Testing the following code
name = ''  
while not name:
    print('Enter your name:')  
    name = input()  
    print('How many guests will you have?')  
    numOfGuests = int(input() or 0)  
    if numOfGuests:  
        print('Be sure to have enough room for all your guests.')  
print('Done')