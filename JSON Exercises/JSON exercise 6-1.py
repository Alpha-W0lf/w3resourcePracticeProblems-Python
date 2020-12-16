# Write a program to create a new JSON file from an existing JSON file.

import json

with open('states.json') as json_file:
    x = json.load(json_file)

# print(x)

y = json.dumps(x, indent=2)

print(y)