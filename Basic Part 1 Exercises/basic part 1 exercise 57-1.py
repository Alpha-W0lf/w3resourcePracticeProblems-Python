# Write a Python program to get execution time for a Python method.

import timeit

start = timeit.timeit()
print("Testing how long this takes to process.")
end = timeit.timeit()

print(end - start)

import time

start = time.time()
print("Testing how long this takes to process using \"time\" module")
end = time.time()

print(end - start)