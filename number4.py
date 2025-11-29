while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")

# can use these line of code or the code in number3.py to get the same results.