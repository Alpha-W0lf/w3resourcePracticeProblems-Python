# Write a Python program to get height and width of the console window.

import fcntl, termios, struct

# rows, columns = os.popen("stty size", "r").read().split()

# print(os.get_terminal_size())

# def terminal_size():
#     th, tw, hp, wp = struct.unpack("HHH", fcntl.ioctl(0, termios.TIOCGWINSZ, struct.pack("HHH", 0, 0, 0, 0)))
#     return tw, th
#
# print("Number of columns and rows in console window: ", terminal_size())

import os
