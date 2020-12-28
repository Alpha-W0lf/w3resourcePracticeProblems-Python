# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'poor' follows the 'not', replace the whole 'not'...'poor' substring with 'good'. Return the
# resulting string.
# Go to the editor
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

def sub_find(given):
    if given.find('not') == True:
        not_loc = given.find('not')
        if given.find('poor') == True:
            poor_loc = given.find('poor')
            if not_loc < poor_loc:
                print("PROGRESS")
            else:
                continue
        else:
            continue
    else:
        continue


sub_find('The lyrics is not that poor!')