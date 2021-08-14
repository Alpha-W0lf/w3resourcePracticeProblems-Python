# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))

sum = x + y
difference = abs(x - y)

print("Sum:", sum, "Difference:", difference)

if sum == 5 or difference == 5 or difference == 0:
    answer = True
else:
    answer = False
print(answer)