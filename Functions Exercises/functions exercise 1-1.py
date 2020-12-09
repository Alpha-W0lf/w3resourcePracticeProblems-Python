# Write a function to find the maximum of three numbers. DONE
# Feature: generate 3 random numbers. DONE

import random

x = random.randint(0, 99)
y = random.randint(0, 99)
z = random.randint(0, 99)
list = [x, y, z]

def find_max():
    print(list)
    maximum = max(list)
    print(maximum)

find_max()