# Write a Python program which accepts the user's first and last name and print them in reverse order with a space
# between them.

full_name = str(input('Enter your first and last name: '))

split_name_list = str.split(full_name, " ")

revered_name_list = split_name_list[::-1]

answer = " "
answer = answer.join(revered_name_list)

print(revered_name_list)
print(answer)