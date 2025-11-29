names = []

with open("names2.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")

# To reverse the sorted names.