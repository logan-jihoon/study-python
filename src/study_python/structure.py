import pprint

### Python practice
dog = {'name ': 'gongju', 'age': 2, 'color':'black'} # Example dictionary

'''
we can create a list of dictionary
'''
allDogs = []  # Empty list for list of dictionaries
allDogs.append({'name ': 'wangja', 'age': 2, 'color':'brown'}) 
allDogs.append({'name ': 'random', 'age': 1, 'color':'black'}) 

print(allDogs)



### Dictionary Data Structure Example
'''
For tic tac toe game, Create a simple dataset using dictionary
'''
theBoard = {'t-L':' ', 't-M':' ','t-R':' ','m-L':' ', 'm-M':' ','m-R':' ','l-L':' ', 'l-M':' ','l-R':' '}

pprint.pprint(theBoard)

### Asign a value to see 
theBoard['m-M'] = 'X'
theBoard['m-L'] = 'X'
theBoard['l-M'] = 'O'


pprint.pprint(theBoard)


### function to draw by taking dictionary as input
def printBoard(board):
    print(board['t-L'] + ' | ' + board['t-M'] + ' | ' + board['t-R']) 
    print('---------')
    print(board['m-L'] + ' | ' + board['m-M'] + ' | ' + board['m-R']) 
    print('---------')
    print(board['l-L'] + ' | ' + board['l-M'] + ' | ' + board['l-R']) 

printBoard(theBoard)


