# Write a Python program to get the volume of a sphere with radius 6.

import math

r = float(input("Enter radius of sphere: "))

volume = (4/3)*(math.pi)*(r**3)

print("The volume of this sphere is:", volume)