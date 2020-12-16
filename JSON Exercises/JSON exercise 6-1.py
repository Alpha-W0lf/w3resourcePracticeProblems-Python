# Write a program to create a new JSON file from an existing JSON file.

import json

with open('states.json') as f:
    x = json.load(f)

for state in x['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(x, f, indent=2)

print(new_states.json)