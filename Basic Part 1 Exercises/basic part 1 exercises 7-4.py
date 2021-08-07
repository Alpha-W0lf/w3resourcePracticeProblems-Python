# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

file_name = input("Enter a filename with \".filename\" at the end: ")

list_file_name = file_name.split(".")

print(list_file_name[1])