# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)

yy = now.year
mm = now.month

print(calendar.month(yy, mm))

# DONE