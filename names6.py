with open("names2.txt") as file:
    for line in sorted(file):
        print("hello,", line.rstrip())

# simpler version of names5.py -- more compact