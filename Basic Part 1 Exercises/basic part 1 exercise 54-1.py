# Write a Python program to get the current username

import os
import getpass

print(os.environ.get("USERNAME"))
print(getpass.getuser())