import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")



# argument parser
# ArgumentParser() is a constructor for a class called ArgumentParser that comes within the Python library.
# parser.add_argument() -- a method in the parser object
# args = parser.parse_args() -- by default parse_args() will automatically look sys argv. No need to import sys.
# args -- is an object.
# args. in loop -- dot is a syntax to access things like properties inside an object.
# args.n -- it contains the integer the human type, after space after -n
# type in command line: python meows8.py -h -- for help.
