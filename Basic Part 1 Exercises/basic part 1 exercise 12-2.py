# Write a program to print the calendar of a given month and year.

import calendar

def convert(yy, mm):
    print(calendar.month(yy, mm))

convert(2004, 2)