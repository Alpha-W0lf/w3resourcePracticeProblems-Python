# Write a python program to get the path and name of the file that is currently executing.

import pathlib

print(pathlib.Path(__file__).resolve())