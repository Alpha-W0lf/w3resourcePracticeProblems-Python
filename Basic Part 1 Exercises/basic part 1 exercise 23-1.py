# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2.

given = str(input("Please enter a string: "))


def copies(n):
    if len(given) > 2:
        print(given[:2] * n)
    else:
        print(given * n)


copies(4)