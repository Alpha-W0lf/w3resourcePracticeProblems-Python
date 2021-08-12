# Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times
# of their sum.

given1 = int(input("Enter a number: "))
given2 = int(input("Enter a number: "))
given3 = int(input("Enter a number: "))

sum = given1 + given2 + given3

if given1 == given2 == given3:
    sum = sum*3

print(sum)