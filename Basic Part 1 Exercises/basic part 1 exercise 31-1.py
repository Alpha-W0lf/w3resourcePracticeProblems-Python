# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

from math import gcd

int1 = int(input("Enter a positive integer. (A negative integer will be converted to positive anyway): "))
int2 = int(input("Enter another positive integer. (A negative integer will be converted to positive anyway): "))

print(gcd(int1, int2))