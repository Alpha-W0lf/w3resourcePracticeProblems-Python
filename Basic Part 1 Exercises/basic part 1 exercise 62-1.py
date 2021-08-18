# Write a Python program to convert all units of time into seconds.

days = float(input("Enter number of days: ")) * 24 * 60 * 60
hours = float(input("Enter number of hours: ")) * 60 * 60
minutes = float(input("Enter number of minutes: ")) * 60
seconds = float(input("Enter number of seconds: "))

total_time = days + hours + minutes + seconds

print("The total amount of time entered is:", total_time, "seconds.")