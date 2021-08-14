# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

int1 = int(input("Enter an integer: "))
int2 = int(input("Enter another integer: "))

sum = int1 + int2

if 15 <= sum <= 20:
    print("The sum is between 15 and 20 so we are returning 20.")
else:
    print("The sum is", sum)