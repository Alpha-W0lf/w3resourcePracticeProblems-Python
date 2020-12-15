# Write a Python program to remove the nth index character from a nonempty string. DONE

input_string = str(input('Enter a string: '))


def remove_nth(given, n):
    final = given[:n] + given[n+1:]
    print(final)


remove_nth(input_string, 4)