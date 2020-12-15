# Write a program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'poor' follows the 'not', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string. DONE
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

# First, find substring 'not'. if no match, return unchanged string. DONE
# Second, find substring 'poor'. if no match, return unchanged string. DONE
# Third, if 'poor' is found after 'not, replace ('not'...'poor') with 'good'. DONE

import re

phrase1 = 'The lyrics is note that pore!\nThe lyrics is not poors!'


def notpoortogood(phrase):
    if phrase.find('not'):
        if phrase.find('poor'):
            phrase = re.sub('(?s)not\W+.+poor\W*', 'good', phrase)
            print(phrase)
        else:
            print(phrase)
    else:
        print(phrase)


notpoortogood(phrase1)