# Write a program to reverse a string.
# Extra feature: generate a random string.

phrase = str(input('Enter some text: '))
print(phrase)

def reverse():
    new_phrase = phrase[::-1]
    print(new_phrase)

reverse()