# Write a program to count the number of characters (character frequency) in a string.

phrase = str(input('Enter a phrase: '))

all_count = {}

for i in phrase:
    if i in all_count:
        all_count[i] += 1
    else:
        all_count[i] = 1

print(all_count)