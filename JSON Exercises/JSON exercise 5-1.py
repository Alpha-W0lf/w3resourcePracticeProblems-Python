# Write a program to convert JSON encoded data into Python objects. DONE

import json

json_obj_1 = '{"workers":[{"firstname":"Sarah", "lastname":"Connor"},{"firstname":"Brian", "lastname":"Williams"},{"firstname":"Todd", "lastname":"Baker"}]}'

json_obj = '{"name" : "John", "age" : 45, "city" : "Austin"}'

py_obj_1 = json.loads(json_obj_1)
py_obj = json.loads(json_obj)
print(py_obj_1)
print(py_obj)