# Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

given = input("Enter a list of numbers separated by spaces: ")

given_list = given.split(" ")
# for i in range(0, len(given_list)):
#     given_list[i] = int(given_list[i])

def check(x):
    x = str(x)
    contained = False

    for i in range(0, len(given_list)):
        if given_list[i] == x:
            contained = True
            print(contained)


check(4)