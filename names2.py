name = input("What's your name? ")

with open("names2.txt", "a") as file:
    file.write(f"{name}\n")


# To store data at names2.txt
# with will open and close the file automatically
# "w" is for write
# "r" is for read mode -- to load not to save it
# "a" is for append
# as file -- this is the return value
#  rm names2.txt -- to remove the names2.txt