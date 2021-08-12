# Write a Python program to test whether a number is within 100 of 1000 or 2000.

given = int(input("Enter a number: "))

range = 100
number1 = 1000
number2 = 2000

lowerBound1 = number1 - range
upperBound1 = number1 + range

lowerBound2 = number2 - range
upperBound2 = number2 + range

if given >= lowerBound1 and given <= upperBound1:
    print(given, "is within", range, "of", number1)
elif given >= lowerBound2 and given <= upperBound2:
    print(given, "is within", range, "of", number2)
else:
    print(given, "is not within", range, "of", number1, "or", number2)