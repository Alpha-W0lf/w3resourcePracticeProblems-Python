# Write a program to get a single string from two given strings separated by a space and swap the first two
# characters of each string.
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

# string_1 = str(input('Enter the first string: '))
# string_2 = str(input('Enter the second string: '))


def char_change(string_1, string_2):
    char1 = string_1[0]
    char2 = string_2[0]
    print(char2+string_1[1:], char1+string_2[1:])


char_change('bou', 'yut')