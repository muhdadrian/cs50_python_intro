with open("names2.txt", "r") as file:
    lines = file.readlines()

for line in lines:# lines is list, line is variable.
    print("hello, ", line.rstrip())



# The second line is reading all the lines and storing the values inside lines.