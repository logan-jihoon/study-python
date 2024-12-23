# This is python code for for loop with list

for i in range(1,5):
    print(i)


range(4)

for i in [1,2,3,4]:
    print(i)


# make the range into list by using a list function

list(range(4))

spam = list(range(0,100,2))
print(spam)
#[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

supplies = ['pen', 'staple','flame-throwers', 'binders']

for i in range(len(supplies)):
    print ('index ' + str(i) + ' in supplies is: ' + supplies[i])



