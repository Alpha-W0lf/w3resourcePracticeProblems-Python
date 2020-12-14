# Write a program to get a string made of the first 2 and the last 2 characters from a given string. If the string
# length is less than 2, return "Empty String" instead. DONE

given = str(input('Enter a string: '))
print(given)

if len(given) < 2:
    print('Empty String')
else:
    print((given[:2])+(given[-2:]))