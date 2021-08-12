# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an
# appropriate message to the user.

given = float(input("Enter a number: "))

if given % 2 == 0:
    print("The number is even.")
elif given % 2 == 1:
    print("The number is odd.")
else:
    print("The number is not an integer.")