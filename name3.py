import sys

if len(sys.argv) < 2: #two arguments: the name of the program [0] and the name of human [1]
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")
else:
    print("hello, my name is", sys.argv[1])

"""
-python name3.py "Adrian Nandu" -- to support two names by putting double quotes,
as sys.argv is a list.
-hello, my name is Adrian Nandu.
"""



