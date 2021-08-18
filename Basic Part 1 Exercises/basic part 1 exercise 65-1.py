# Write a Python program to convert seconds to day, hour, minutes and seconds.

import time

given = int(input("Enter number of seconds: "))

days = given / (3600 * 24)
days = int(days)
remainder = given % (3600 * 24)

hours = remainder / (60 * 60)
hours = int(hours)
remainder = remainder % (60 * 60)

minutes = remainder / 60
minutes = int(minutes)
remainder = remainder % 60

seconds = remainder

print("That number of seconds is equal to", days, "days,", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")