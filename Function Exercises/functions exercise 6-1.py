# Write a function to check whether a number is in a given range DONE

def checking(range_start, range_end):
    our_range = range(range_start, range_end)
    num = float(input('Please enter a number to see if it is in the given range: '))
    in_range = 'This number IS NOT in the given range.'
    for x in our_range:
        if num == x:
            in_range = 'This number IS in the given range.'
            break
        else:
            continue
    print(in_range)

checking(0, 99)