# Write a program to count the number of characters (character frequency) in a string.

phrase = str(input('Enter a phrase: '))

all_freq = {}

for i in phrase:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

print (all_freq)