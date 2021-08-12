# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return
# double the absolute difference

given = float(input("Enter a number: "))

if given > 17:
    answer = abs(given - 17) * 2
    print(answer)
else:
    answer = abs(17 - given)
    print(answer)

