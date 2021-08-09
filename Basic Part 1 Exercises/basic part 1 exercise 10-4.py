# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

given = int(input("Enter an integer: "))

x_1 = given

x_2 = int(str(given) + str(given))

x_3 = int(str(given) + str(given) + str(given))

answer = x_1 + x_2 + x_3

print(answer)