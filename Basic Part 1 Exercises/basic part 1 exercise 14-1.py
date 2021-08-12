# Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

# from random import randrange
# from datetime import timedelta
#
# def random_date(start, end):
#     delta = end - start
#     int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
#     random_second = randrange(int_delta)
#     return start + timedelta(seconds=random_second)
#
# random_date()
#
# date1 = (2014, 7, 2)
# date2 = (2014, 7, 11)
#
# difference = date1[2] - date2[2]
# answer = abs(difference)
# print(answer)

from datetime import date
date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
difference = date2 - date1
print(difference.days)