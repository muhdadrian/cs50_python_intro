import sys

if len(sys.argv) == 1: #no argument
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows7.py")

# in command line type: python meows7.py -n 3