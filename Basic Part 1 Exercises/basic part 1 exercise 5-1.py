# Write a program which accepts the user's first and last name and print them in reverse order with a space between
# them. DONE

first = input('What\'s your first name? ')
last = input('What\'s your last name? ')

first_rev = first[::-1]
last_rev = last[::-1]

print(first_rev)
print(last_rev)
print('Here is your name reversed:', first_rev, last_rev)
print(last_rev, first_rev)
