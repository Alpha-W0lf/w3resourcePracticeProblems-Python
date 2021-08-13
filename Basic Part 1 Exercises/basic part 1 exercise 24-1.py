# Write a Python program to test whether a passed letter is a vowel or not.

letter = str(input("Enter a letter: "))


def vowel(x):
    if len(x) > 1:
        print("Input is more than one character.")
    elif x.lower() in ["a", "e", "i", "o", "u"]:
        print("Letter is a vowel.")
        print(x.lower())
    else:
        print("Letter is not a vowel.")
        print(x.lower())


vowel(letter)