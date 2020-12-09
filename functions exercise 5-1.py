# Write a function to calculate the factorial of a number (non-neg integer). The function accepts the number as an
# argument. DONE


def factorial_calc(i):
    i = abs(i)
    our_list = list(range(1, i + 1))
    result = 1
    for x in our_list:
        result = result * x
        continue
    print('The factorial of', i, 'is:')
    print(result)


factorial_calc(6)
