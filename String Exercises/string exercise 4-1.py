# Write a program to get a string from a given string where all occurrences of its first char have been exchanged to
# '$', except the first occurrence of the char itself. DONE
# Ex. Sample String: 'restart'
# Ex. Expected Result: 'resta$t'

# phrase = str(input('Enter a string: '))

# for x in phrase:
#     if x == phrase[:1]:
#         x = '0'
#     else:
#         x = x
#
# print(phrase)
# print(phrase[0])


# def char_change(phrase):
#     char = phrase[0]
#     phrase = phrase.replace(char, '$')
#     phrase = char + phrase[1:]
#     print(phrase)
#
# char_change('restart')


def char_change(phrase):
    char = phrase[0]
    phrase = phrase.replace(char, '$')
    phrase = char + phrase[1:]
    print(phrase)


char_change('restart')