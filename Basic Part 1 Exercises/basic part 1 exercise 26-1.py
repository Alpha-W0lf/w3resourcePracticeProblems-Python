# Write a Python program to create a histogram from a given list of integers.

given = input("Enter a list of integers separated by spaces: ")
given_list = given.split(" ")
print(given_list)

for i in range(0, len(given_list)):
    given_list[i] = int(given_list[i])

print(given_list)


def histogram(x):
    for i in x:
        print("*"*i)


histogram(given_list)