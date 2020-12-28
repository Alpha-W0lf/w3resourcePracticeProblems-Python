# Write a Python program to get a string from a given string where all occurrences of its first char have been
# changed to '$', except the first char itself. Go to the editor
# Sample String : 'restart'
# Expected Result : 'resta$t'

given = str(input('Enter a string: '))
first_char = given[:1]
print(first_char)

# for x in given[1:]:
#     if x == first_char:
#         x = '$'
#         print(x)
#     else:
#         continue
#
# print(given)

answer = given[1:].replace(given[:1], '$')
print(first_char+answer)

# DONE