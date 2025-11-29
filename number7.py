def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()

# this is simplified version of number6.py -- less code
# come up with good reason in coding, and it will come with experience and practice - David Malan.
