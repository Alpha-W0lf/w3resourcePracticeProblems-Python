# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

int1 = int(input("Enter an integer: "))
int2 = int(input("Enter a second integer: "))
int3 = int(input("Enter a third integer: "))

check_set = set([int1, int2, int3])

print(check_set)
print(len(check_set))

if len(check_set) == 3:
    print("The sum of the integers is", int1 + int2 + int3)
else:
    print("There are duplicates, so we are returning the sum as 0")