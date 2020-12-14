# Write a function that takes a list and returns a new list with unique elements of the first list DONE
import random


def list_mix(original):
    print(original)
    random.shuffle(original)
    cleaned_list = list(set(original))
    print(cleaned_list)

list_mix([1, 2, 3, 3, 3, 3, 4, 5, 6])