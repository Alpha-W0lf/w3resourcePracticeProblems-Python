# Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

import platform, struct

print(platform.architecture())
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)