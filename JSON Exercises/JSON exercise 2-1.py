# Write a Python program to convert Python object to JSON data. DONE

import json

x = {
    "name":"Jason",
    "age":31,
    "city":"Austin"
}

y = json.dumps(x)

print(y)