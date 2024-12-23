#function call with list
### Passing list in function calls

### Define a randome funtion that add a value to a list
def eggs(someParameter):
    someParameter.append('Hello')

spam = [1,2,3]
eggs(spam)  # so the local parameter will be destroyed, but it works. Why?
print(spam) # [1, 2, 3, 'Hello']

### So even though someParameter variable is destoryed, since it's referencing to the same refernce, it does affect the global scope outcome too
### Careful changing Mutable data type such as list



### copy module : Copy a list
import copy
spam = ['a','b','c','d']
cheese = copy.deepcopy(spam)  # create a brand new list instead of referencing it
cheese[1] = 42  # so modifying cheese won't affect spam
print(cheese)
print(spam)


### List continuation
'''
list can span in multiple lines of code
'''

spam = ['apples',
        'oranges',
        'bananas',
        'cats']

print(spam)  #['apples', 'oranges', 'bananas', 'cats']

### \ continuation function
print('Four score and seven ' + \
    'years ago')  # \ tells python to ignore the indentation coming up the next line