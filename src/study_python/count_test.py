#This is a simple python program to count : characters and words
import pprint  # for the better print format

### Create a message
message = 'It was a bright cold day in April, and the clocks'

### Create a count dictionary for characters: Key is each letter and value is count 
count = {}

for characters in message:
    count.setdefault(characters, 0)  # to create a letter key and assign 0 value
    count[characters] +=1 # For the letter key's value, add +1

print(count)


### Create a count dictionary for words: Key is each words and value is count 
count = {}

for words in message.split():  # Use .split() method for str
    count.setdefault(words, 0)  # to create a letter key and assign 0 value
    count[words] +=1 # For the letter key's value, add +1

print(count)



rjtext = pprint.pformat(count)
print(rjtext)