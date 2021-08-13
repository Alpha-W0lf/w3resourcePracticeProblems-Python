# Write a Python program to concatenate all elements in a list into a string and return it.

def concatinate(x):
    output = ""
    for i in x:
        output = output + str(i)

    print(output)


concatinate([12, "us", 2, 3, 4])