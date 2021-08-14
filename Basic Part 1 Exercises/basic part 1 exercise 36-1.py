# Write a Python program to add two objects if both objects are an integer type.

def check_type(obj1, obj2):
    if type(obj1) and type(obj2) == int:
        print(obj1 + obj2)
    else:
        print("These are not both integers.")

check_type(23, -3.3)