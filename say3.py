import sys

# Find sayings.py file and read from top to bottom and find specific function of hello.
from sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])