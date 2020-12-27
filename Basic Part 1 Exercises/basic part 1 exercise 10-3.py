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
        concat = given*count
        answer_list.append(int(concat))
        count += 1
    print(sum(answer_list))


n1 = int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))

print('Reproducing solution:', n1+n2+n3)
strange_add(n, digits)

# DONE