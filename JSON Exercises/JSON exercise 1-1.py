# Write a Python program to convert JSON data to Python object. DONE

import json

x = '{"name":"Brian", "age":31, "city":"Austin"}'
y = json.loads(x)
print(y)
print(y["age"])