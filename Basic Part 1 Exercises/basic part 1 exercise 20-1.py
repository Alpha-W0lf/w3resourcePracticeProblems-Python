# Write a Python program to get a string which is n (non-negative integer) copies of a given string.

given = str(input("Enter a string: "))


def multiply(n):
    print(abs(n)*given)


multiply(-3)