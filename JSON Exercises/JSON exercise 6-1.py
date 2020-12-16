# Write a program to create a new JSON file from an existing JSON file. DONE

import json

with open('states.json') as f:
    x = json.load(f)

for state in x['states']:
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(x, f, indent=2)

# TODO - Need to revisit/keep practicing JSON