import cowsay
import sys #to run command-line

if len(sys.argv) == 2: #the name of the program and first name
    cowsay.cow("hello, " + sys.argv[1])


# pip install cowsay