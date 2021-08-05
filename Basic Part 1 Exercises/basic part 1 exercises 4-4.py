# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# Area = pi r ^ 2

import math

r = float(input("Enter the radius of the circle:"))

area = (math.pi * r * r)

print("The area for a circle with radius" + r + "is" + area)
