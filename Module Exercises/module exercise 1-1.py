# Write a Python program to generate a random color hex, a random alphabetical string, random value between two
# integers (inclusive) and a random multiple of 7 between 0 and 70. Use random.randint()

import random
import string

random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))
max_length = 255
random_string = ""
for i in range(random.randint(1, max_length)):
    random_string += random.choice(string.ascii_letters+string.digits)

random_int = random.randint(4, 99)
random_mult7 = random.randint(0, 10) * 7

print(random_color)
print(random_string)
print(random_int)
print(random_mult7)