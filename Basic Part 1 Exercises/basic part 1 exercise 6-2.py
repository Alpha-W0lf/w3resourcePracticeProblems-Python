# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.

sequence = str(input('Enter a sequence of comma-separated numbers: '))


def converter(string):
    our_tuple = tuple(string.split(', '))
    our_list = list(string.split(', '))
    print(our_tuple, '\n', our_list, sep='')

converter(sequence)

# DONE