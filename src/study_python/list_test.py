#This is a program to see the simliarities between list and string

### Lists and Strings : Simmilarity
print(list('Hello'))
name = 'Zophie'
print(name[0]) #'Z'
print(name[1:3]) #'op'

### in operator works too
print('Zo' in name)  # True
print('xxx' in name) # False


### for loop
for letters in name:
    print(letters)


### Lists and Strings : Difference - List is mutable and String is immutalbe
name = 'Zophie the cat'
print(name[7]) # 't'  

'''
name[7] = 'x'  is not working as name[7] is str and it's not mutable
'''


### Then how to modify a str : Using Slices
name = 'Zophie a cat'
newName = name[0:7] + 'the' + name[8:12]  #Slices and concat
print(newName)





### references
spam = 42
cheese = spam  
spam = 100  # Reassign the vale of spam
print(cheese)  #42 instead of 100. Bc of how reference works


### How does referencing work
spam = [0,1,2,3,4,5] # When we assign this list value to spam, it create a list and assign its reference to spam
cheese = spam  # Cheese is referencing to the same list
cheese[1] = 'Hello'  # it changes the list value of the reference that both cheese and spam are referencing  

print(cheese) # [0, 'Hello', 2, 3, 4, 5] 
print(spam) # [0, 'Hello', 2, 3, 4, 5]  SO, this mutable feature can create errors



