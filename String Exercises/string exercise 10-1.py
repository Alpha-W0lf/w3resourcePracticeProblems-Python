# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
# DONE

# original = str(input('Enter a string: '))
# print(original)
#
# final = original[-1] + original[1:-1] + original[0]
# print(final)

# Now do it using a function. DONE

original = str(input('Enter a string: '))
print(original)


def char_swap(given):
    final = given[-1] + given[1:-1] + given[0]
    print(final)


char_swap(original)