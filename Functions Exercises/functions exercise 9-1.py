# Write a function that takes a number as a parameter and check if the number is prime or not. DONE


def find_prime(num):
    print(num)
    divisible = False

    for x in range(2, (num-1)):
        if num % x == 0:
            divisible = True
            print('Number is NOT PRIME!')
            break
        else:
            continue
    if not divisible:
        print('Number IS PRIME!')

find_prime(710)