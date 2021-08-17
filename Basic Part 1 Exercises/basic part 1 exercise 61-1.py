# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

given = float(input("Enter a distance in feet: "))

print("That is", (given*12), "inches.")
print("That is", (given/3), "yards.")
print("That is", (given/5280), "miles.")