# Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
# Sample Output :
# r = 1.1
# Area = 3.8013271108436504

# Area = pi r ^ 2

import math

r = float(input("Enter the radius of your circle: "))
area = (r ** 2) * math.pi
print("The area of your circle is: " + str(area))