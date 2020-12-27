# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

n = int(input('Enter an integer: '))
digits = int(input('Enter the number of digits for the answer: '))


def strange_add(given, length):
    count = 1
    answer_list = []
    given = str(given)

    while count <= length:
        answer_list.append(given*count)
        count += 1
    print(sum(answer_list))


strange_add(n, digits)