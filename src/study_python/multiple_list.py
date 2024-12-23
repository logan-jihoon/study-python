### Multiple assignment : The following list can be simplified

cat = ['fat','orange','loud']

size = cat[0]
color = cat[1]
disposition = cat[2]

### The above can be simplified to 
size, color, disposition = cat

print(cat)

size, color, disposition = 'skinny', 'black','quiet'


### Swap Variable : using multiple assignment
a = 'AAA'
b = 'BBB'

a,b = b,a

print(a)
print(b)


### Augmented assignment operator
spam = 42
spam = spam +1  #  instead of this

spam = 42
spam +=1  # Results in the same thing


print(spam)



