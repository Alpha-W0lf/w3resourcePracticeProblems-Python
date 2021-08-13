# Write a Python program to count the number 4 in a given list.

given = input("Provide a list separated by spaces: ")

given_list = given.split(" ")

count = 0

for i in given_list:
    if i == "4":
        count += 1
    else:
        continue

print(given_list)
print(count)