# Write a Python program to accept a filename from the user and print the extension of that. Go to the editor
# Sample filename : abc.java
# Output : java

filename = str(input('Please enter a file name ending with \'.extension\': '))
split_filename = filename.split('.')
extension = split_filename[-1]

print(extension)
print('.'+extension)

# DONE