# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. Go to the editor
# Sample value of n is 5
# Expected Result : 615

given = int(input('Enter an integer: '))
# digits = int(input('Enter the total number of digits: '))
#
# def adding(num, spaces):
#     count = 1
#     num = str(num)
#     list = []
#     while count <= spaces:
#         num_step = num*count
#         list.append(int(num_step))
#         count += 1
#     print(list)
#     answer = sum(list)
#     print('The answer is', answer)
#
# adding(given, digits)

n1 = int("%s" % given)
n2 = int("%s%s" % (given, given))
n3 = int("%s%s%s" % (given, given, given))

answer = n1+n2+n3
print(answer)

# DONE