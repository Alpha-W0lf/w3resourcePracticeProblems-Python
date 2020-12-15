# Write a program to convert JSON encoded data into Python objects.

import json

json_obj = {
    "workers" : [
        {"firstname" : "Sarah", "lastname" : "Connor"},
        {"firstname" : "Brian", "lastname" : "Williams"},
        {"firstname" : "Todd", "lastname" : "Baker"}
    ]
}

py_obj = json.load(json_obj)