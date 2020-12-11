# Write a program to accept a filename from the user and print the extension of that.

filename = input('Enter a filename with a .extension: ')
filename_list = filename.split('.')
print(filename_list)
print(filename_list[1])