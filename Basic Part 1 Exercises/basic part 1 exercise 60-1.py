# Write a Python program to calculate the hypotenuse of a right angled triangle.

# a ** 2 + b ** 2 = c ** 2

from math import sqrt

height =  float(input("Enter the height of the triangle: "))
length = float(input("Enter the length of the triangle: "))


def triangle(x, y):
    hypo = sqrt((height ** 2) + (length ** 2))
    print(hypo)


triangle(height, length)