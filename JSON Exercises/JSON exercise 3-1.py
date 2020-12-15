# Write a program to convert Python objects into JSON strings. Print all the values. DONE

import json

py_obj = {
    "name" : "John",
    "age" : 35,
    "occupation" : "Sales",
    "city" : "Austin",
}

json_obj = json.dumps(py_obj)

print(json_obj)