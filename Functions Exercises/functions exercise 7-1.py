# Write a function that accepts a string and calculate the number of upper case letters and lower case letters DONE

def count_letters(phrase):
    # phrase = str(input('Enter a string: '))
    upper_count = sum(map(str.isupper, phrase))
    lower_count = sum(map(str.islower, phrase))
    print('There are', upper_count, 'upper case letters and', lower_count, 'lower case letters in this phrase.')

count_letters('WATER and FIRE do not mix')