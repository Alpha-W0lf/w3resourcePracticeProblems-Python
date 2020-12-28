# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'poor' follows the 'not', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string.
# Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def sub_find(given):
    if given.find('not') >= 0:
        not_loc = given.find('not')
        if given.find('poor', not_loc) >= 0:
            poor_loc = given.find('poor')
            given_new = given.replace('poor', 'good')
            print(given[:not_loc]+given_new[poor_loc:])
            print(given_new)
        else:
            print(given)
    else:
        print(given)


sub_find('The lyrics is not that poor!')