# Write a Python program to get file creation and modification date/times.

import os
import time

time_create = os.path.getctime("basic part 1 exercise 64-1.py")
time_mod = os.path.getmtime("basic part 1 exercise 64-1.py")

print(time_create, time_mod)

time_create_final = time.ctime(time_create)
time_mod_final = time.ctime(time_mod)

print(time_create_final, time_mod_final)