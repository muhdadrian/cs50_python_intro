import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")

# This will prevent the error from occuring when we only type: python name2.py, without any argument after name2.py like in name.py.