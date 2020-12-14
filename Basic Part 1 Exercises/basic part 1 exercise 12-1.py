# Write a program to print the calendar of a given month and year. TODO

import calendar

month = str(input('INPUT -- Enter a 3 letter abbreviation for a month: '))
year = str(input('INPUT -- Enter a 4 digit year: '))
month = month.lower()


def convert_month(mmm):
    abbrev_month = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    month_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    mm_format = False

    for x in abbrev_month:
        if x == mmm:
            mm_format = True
            month_final = int(abbrev_month.index(x))
            mm = month_num[month_final]
            # print('Month code:', mm)
            return mm
        else:
            continue
    if not mm_format:
        mmm = str(input('RETRY -- Enter a 3 letter abbreviation for a month: '))
        convert_month(mmm)


convert_month(month)

# Make a function to accept either yy or yyyy format. Prompt user to re-enter if not.


def convert_year(yyy):
    yy_format = False
    while not yy_format:
        if len(yyy) == 4:
            yy_format = True
            yy = int(yyy)
            # print('Year code from 4 digits:', yy)
            return yy
        else:
            yyy = input('RETRY -- Enter a 4 digit year: ')
            convert_year(yyy)


convert_year(year)

print(calendar.month(convert_year(year), convert_month(month)))

# Need to make sure years like 2003 are not converted to 3...need them to be 03 DONE
# Need to make sure 'Year code' and 'Month code' text prints are not duplicated DONE