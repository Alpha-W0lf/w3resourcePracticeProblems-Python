# Write a Python program to count the number of characters (character frequency) in a string. Go to the editor
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#
# given = str(input('Enter a string: '))
#
#
# def char_count(string):
#     given_dict = {}
#     for x in string:
#         keys = given_dict.keys()
#         if x in keys:
#             given_dict[x] += 1
#         else:
#             given_dict[x] = 1
#     print(given_dict)
#
#
# char_count(given)

# Redoing it to practice more! \|/ \|/

given = str(input("Enter a string: "))

def char_count(string):
    given_dict = {}
    for x in string:
        keys = given_dict.keys()
        if x in keys:
            given_dict[x] += 1
        else:
            given_dict[x] = 1
    print(given_dict)

char_count(given)

# DONE