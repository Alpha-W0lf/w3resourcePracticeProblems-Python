# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math


def distance(x, y):
    len0 = abs(x[0] - y[0])
    len1 = abs(x[1] - y[1])
    print(len0, len1)
    answer = math.sqrt((len0 ** 2) + (len1 ** 2))
    print(x, y)
    print("The distance between the two points is", answer)

distance((2, 3), (5, 7))