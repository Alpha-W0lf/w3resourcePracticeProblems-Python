# Write a Python program to get OS name, platform and release information.

import platform, os

print(os.name)
print(platform.system())
print(platform.architecture())
print(platform.platform())
print(platform.release())