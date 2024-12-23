#simple test of list 

#spam list
spam = [['cat','bat'],[10,20,30,40,50]]

print(spam[0][1])
# The output is going to be 'bat'

spam = [1,4,2,5]

print(spam[1:3])
#the output is [4,2]


spam[2]='Hello'

print(spam)
#[1, 4, 'Hello', 5]

print(spam[:2])
#[1,4]

del spam[2]
print(spam)

#[1,4,5]

