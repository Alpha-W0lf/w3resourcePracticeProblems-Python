# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

filename = str(input('Enter a filename (including the .extension: '))

def extract_extension(file):
    extension = list(filename.split('.'))
    print(extension[-1])

extract_extension(filename)

# DONE