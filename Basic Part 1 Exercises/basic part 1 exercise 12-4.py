# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar

def converter(yy, mm):
    print(calendar.month(yy, mm))

converter(2007, 12)