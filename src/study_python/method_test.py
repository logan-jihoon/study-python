### This is a simple ptyhon program related to multiple assignment & List method

### Multiple Assignemnt : Tuple Unpacking 
size, color, disposition = 'skinny', 'black', 'quiet'

### OR We can use the following
cat = ['fat','oragne','loud']  # Define a variale with a list value
size, color, disposition = cat   # Define variales by assgining values from the list

print(size)

### The multiple assignemnt only works as long as python knows the left side of = is a vralid target. The below does not work
'''
'hello', 'hi','howdy'= cat
'''



### Augmented Operation
spam = 42
spam +=1  #spam = spam +1   Works in the same way
print(spam)


### List Emthod : index
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index('hello'))  # 0 will be return
print(spam.index('heyas'))  # 3 will be return




### To add a new value to a list : append() method
spam = ['cat','dog','bat']
spam.append('moose')  # adding 'moose' on top of the exiting values at the last
print(spam)

spam = ['cat','dog','bat']
spam.insert(1,'chicken')  #inserting chichekn at a position 1
print(spam)  # ['cat', 'chicken', 'dog', 'bat']



### To remove a value from a list

spam = ['cat','dog','bat']
spam.remove('bat')
print(spam) #['cat', 'dog'] is the output


### in case that we have more than one value in the list, it removes the first value 
spam = ['cat','bat','dog','bat']
spam.remove('bat')
print(spam) #['cat', 'dog', 'bat']


### .remove() method is different from del statement. It doesn't need to specify the exact location of the value
spam = ['cat','bat','dog','bat']
del spam[1]  # need to specify the location
print(spam) #['cat', 'dog', 'bat']



### .sort() method

spam = [1,23,5,2,3,6,8]
spam.sort()
print(spam) #[1, 2, 3, 5, 6, 8, 23] Sorted

spam.sort(reverse=True)
print(spam) #[23, 8, 6, 5, 3, 2, 1] Desc sorted

'''
ptyhon does not know how to sort a list with string and numeric values together

spam = [1,2,3,'alice']  This will give us an error
'''


### .sort() for string values
spam = ['a','z','A','Z']
spam.sort()
print(spam) #['A', 'Z', 'a', 'z']

spam.sort(key =str.lower)
print(spam) # ['A', 'a', 'Z', 'z'] Alphabetical order first regarding of the case


