# Write a python program to access environment variables.

import os

os.environ["USER"] = "Tom"

print(os.environ)
print(os.environ.get("USER"))
print("\n\n")
print(os.environ.get("USERNAME"))
print("\n\n")
print(os.environ.get("PATH"))