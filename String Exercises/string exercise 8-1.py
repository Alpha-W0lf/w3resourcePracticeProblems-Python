# Write a Python function that takes a list of words and returns the length of the longest one. Go to the editor DONE
# Sample Output:
# Longest word: Exercises
# Length of the longest word: 9

# given = ['list', 'are', 'festival', 'edm']
#
#
# def return_longest(words):
#     given_len = []
#     for x in given:
#         given_len.append(len(x))
#         print(x)
#     print(given_len)
#     longest_value = 0
#     for y in given_len:
#         if y > longest_value:
#             longest_value = y
#             longest_index = given_len.index(y)
#             print(longest_value)
#             print(longest_index)
#             final = given[longest_index]
#         else:
#             continue
#     print('The longest word is ' + final + '.')
#     print('Its length is ' + str(longest_value) + '.')
#
#
# return_longest(given)

# Clumsy/inefficient way ^^ Going to redo below. DONE

given = ['list', 'are', 'festival', 'edm']
given.sort(key=len)
print(given)
print('The longest word is \"' + given[-1] + '\".')
print('The length of this word is:', len(given[-1]))