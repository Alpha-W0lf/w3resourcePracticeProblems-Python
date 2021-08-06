# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

first = str(input("Enter your first name: "))
last = str(input("Enter your last name: "))

first_list = list(first)
last_list = list(last)

first_list.reverse()
last_list.reverse()


print(first_list)
print(last_list)

def first_list_to_string(x):
    first_rev = ""
    for letter in x:
        first_rev = first_rev + letter
    return first_rev

def last_list_to_string(y):
    last_rev = ""
    for letter in y:
        last_rev = last_rev + letter
    return last_rev

# x = first_list
# y = last_list

print(first_list_to_string(first_list))
print(last_list_to_string(last_list))