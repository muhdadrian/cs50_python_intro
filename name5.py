import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)

# python name5.py Hello Adrian Nandu

"""
python name5.py adrian nandu
hello, my name is adrian
hello, my name is nandu
"""
