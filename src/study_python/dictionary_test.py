# This is python test file for dictionaries

### Dictionary datatype has a key (index for dictionaries). Key value pair
myCat = {'size':'fat', 'color':'gray','disposition':'loud'}
print(myCat['size'])

print('My cat has '+ myCat['color'] + ' fur.')

spam = {121345: 'Luggage combination', 42: 'The answer'}

print(spam)



### Unlike the list where a order matter, dictionaries do not care about the order
print([1,2,3] == [3,2,1]) #False due to differnt orders

gongju = {'name':'gongju','species':'dog','age':2} #gongju and jindo have an exact same values with different orders
jindo = {'species':'dog','age':2,'name':'gongju'}

print(gongju==jindo)  #True

'''
If wrong key, then it will give you an error
gongju['color'] will give us a key error
'''

### in and not in operator in dictionaries
print('name' in gongju)  # True
print('name' not in gongju) # False



### .keys() .values()  .items() method with list like data type
print(list(gongju.keys()))
print(list(gongju.values()))
print(list(gongju.items()))

### .keys() without list function
print(gongju.keys()) #dict_keys

### for loops for dictionaries
for k in gongju.keys():
    print(k)  # name species age

for v in gongju.values():
    print(v)  # gongju dog 2

for k, v in gongju.items():
    print(k,v)  # name gongju species dog  age 2


### Check a value is in a dictionary 
print('dog' in gongju.values()) # True

### How to check if a particular key is in dictionary?.get() method
'''
gongju['color'] will crash the program
Hence, we need to use if 
'''
if 'color' in gongju:
    print(gongju['color'])

'''
But it's super tidious, python provide alternatives
'''
print(gongju.get('color','')) # will return a blank space
print(gongju.get('age',0)) # will return 2. It will find 'age', if it doesn't exit then return 0


picnicItems = {'apples': 5, 'cups':2}
print('I am brining '+ str(picnicItems.get('napkins',0))+ ' to the picnic.')


### .setdefault() method
'''
We can use if to set a default value. But it is tidious
'''

if 'color' not in gongju:
    gongju['color'] = 'black'


'''
The above can be avoided by using .setdefault() method
'''
gongju.setdefault('color','black')

print(gongju)   #{'name': 'gongju', 'species': 'dog', 'age': 2, 'color': 'black'}

