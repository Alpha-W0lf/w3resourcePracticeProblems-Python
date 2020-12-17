# Write a Python program to display the current date and time.

from datetime import datetime

print(datetime.now().date(), datetime.now().strftime("%H:%M:%S"))
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

# DONE