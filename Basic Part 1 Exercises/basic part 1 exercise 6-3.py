# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
# tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

given = input('Please enter a list of numbers separated by commas: ')

given_list_str = given.split(', ')
given_list_int = list(map(int, given.split(', ')))
given_tuple_str = tuple(given.split(', '))
given_tuple_int = tuple(map(int, given.split(', ')))

print(given_list_str)
print(given_list_int)
print(given_tuple_str)
print(given_tuple_int)

# DONE