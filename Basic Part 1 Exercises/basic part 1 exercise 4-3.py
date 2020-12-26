# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

import math

radius = float(input('Enter the radius of a circle: '))
area = math.pi * (radius ** 2)
area_rounded = ("%.2f" % area)

print('The area of the circle is', area_rounded)

# DONE