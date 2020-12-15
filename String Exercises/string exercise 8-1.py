# Write a Python function that takes a list of words and returns the length of the longest one. Go to the editor
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

given = ['list', 'are', 'festival', 'edm']


def return_longest(words):
    given_len = []
    for x in given:
        given_len.append(len(x))
        print(x)
        print(given_len)


# x is the actual element in the list. we need to return the index of the element to build given_len[]

return_longest(given)