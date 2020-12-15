# Write a program to convert Python dictionary object (sort by key) to JSON data. Print the object members with
# indent level 4. DONE

import json

py_dict = {
    "name" : "Paul",
    "age" : "44",
    "city" : "Austin",
    "hobby" : "bike riding"
}

json_dict = json.dumps(py_dict, sort_keys=True, indent=4)

print(json_dict)