# Write a Python program to get a single string from two given strings, separated by a space and swap the first two
# characters of each string. Go to the editor
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'

given_1 = str(input('Enter a string: '))
given_2 = str(input('Enter a second string: '))


def char_swap(str_1, str_2):
    answer = str_2[:2]+str_1[2:]+' '+str_1[:2]+str_2[2:]
    print(answer)


char_swap(given_1, given_2)