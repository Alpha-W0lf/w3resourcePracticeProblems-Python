# Write a Python program to add two objects if both objects are an integer type.

obj1 = 23
obj2 = 33.0

if type(obj1) and type(obj2) == int:
    print(obj1 + obj2)
else:
    print("These are not both integers.")