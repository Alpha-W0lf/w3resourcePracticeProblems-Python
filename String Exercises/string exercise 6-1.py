# Write a program to add 'ing' at the end of a given string (length should be at least 3). If the given string
# already ends with 'ing', then add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

# First, check for length of 3. Do nothing if less than 3. DONE
# Second, check for 'ing' at end and add 'ly' if matches. add 'ing' if not. DONE


def word_mod(word):
    if len(word) < 3:
        print('The string is less than 3 characters so we left it the same:', word)
    else:
        if word[-3:] == 'ing':
            word_changed = word+'ly'
            print('We added \'ly\' and got:', word_changed)
        else:
            word_changed = word+'ing'
            print('We added \'ing\' and got:', word_changed)


word_mod('trucking')