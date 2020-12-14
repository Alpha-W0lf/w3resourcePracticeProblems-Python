# Write a program to print the even numbers from a given list. DONE

our_list = [1, 2, 3, 4, 5, 6, 7, 8]


def spit_even(given):
    answer = []
    for x in given:
        if x % 2 == 0:
            answer.append(x)
        else:
            continue
    print(answer)

# our_list = [1, 2, 3, 4, 5, 6, 7, 8]

spit_even([12, 13, 14, 15, 16, 17, 8, 4, 3])