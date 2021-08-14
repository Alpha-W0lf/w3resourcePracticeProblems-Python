# Write a Python program to get the least common multiple (LCM) of two positive integers.

from math import lcm

int1 = int(input("Enter an integer. (Negative integers will be converted to positive anyway.): "))
int2 = int(input("Enter another integer. (Negative integers will be converted to positive anyway: "))

int1 = abs(int1)
int2 = abs(int2)

print(lcm(int1, int2))