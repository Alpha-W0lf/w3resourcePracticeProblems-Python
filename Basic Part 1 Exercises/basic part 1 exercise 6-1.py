# Write a program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with
# those numbers. DONE

raw_seq = input('Enter a sequence of numbers separated by commas: ')

# list_seq = list(raw_seq)
# for x in list_seq:
#     if x == ' ':
#         list_seq.remove(x)      ## Not sure why ' ' isn't removing spaces. Do I have to import re and use regex?
#                                 ## There has to be a simpler way
#     elif x == ',':
#         list_seq.remove(x)
#     else:
#         continue
# tuple_seq = tuple(list_seq)
# print(list_seq)
# print(tuple_seq)

list_seq = raw_seq.split(', ')
tuple_seq = tuple(list_seq)
print(list_seq)
print(tuple_seq)