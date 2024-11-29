# A program testing while loop

#Test a problematic while loop
name = ''
while name != 'your name':
     print('please type your name')
     name = input()

print('thank you!')



# Test the same problematic while loop with break

while True:
	print('please type your name.')
	name = input()
	if name == 'your name':
		break
print('Thank you!')