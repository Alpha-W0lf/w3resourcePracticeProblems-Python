# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a
# tuple with those numbers. Go to the editor
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

sample_data = input("Enter a sequence of numbers separated by commas: ")

def make_list(x):
    li = list(x.split(", "))
    return li

def make_tuple(y):
    tu = tuple(y.split(", "))
    return tu


print(make_list(sample_data))
print(make_tuple(sample_data))
