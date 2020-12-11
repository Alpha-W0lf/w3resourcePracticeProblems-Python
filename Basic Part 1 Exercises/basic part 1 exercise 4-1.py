# Write a program which accepts the radius of a circle from the user and computes the area. DONE
import math

# radius = float(input('Please enter the radius of your circle: '))
# area = radius * (math.pi ** 2)
#
# print('The area of the circle with radius', radius, 'is:', area)

# Now do it in a function DONE

def circle_area(radius):
    area = radius * (math.pi ** 2)
    print('The area of the circle with radius', radius, 'is:', area)

circle_area(5)