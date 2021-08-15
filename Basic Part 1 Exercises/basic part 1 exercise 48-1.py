# Write a Python program to parse a string to Float or Integer.

given = input("Enter a number: ")

print(type(given))

given = float(given)
print(given, "is now a float.")

given = int(given)
print(given, "is now an integer.")