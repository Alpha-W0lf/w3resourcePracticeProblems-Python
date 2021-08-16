# Write a Python program to sum of the first n positive integers.

given = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]


def sum_num(n):
    answer = 0
    for i in range(given[0], given[n-1]):
        answer = answer + i
    print(given[n-1])
    print(answer)

n = 7
sum_num(n)


x = int(input("Enter a positive integer: "))
sum_x = (x * (x + 1)) / 2
print("The sum of the first", x, "positive integers is:", int(sum_x))