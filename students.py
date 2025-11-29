with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

"""
rstrip -- to remove the whitespace in the end, and the result will be split(", "),
the split function or method comes with str, and any str has this method built-in function to split
based on the comma
"""