# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given
# string already begins with "Is" then return the string unchanged.

given = str(input("Enter a string: "))

if given[0:2] == "Is":
    print(given)
else:
    given_mod = "Is" + given
    print(given_mod)