def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))

meow(number)


"""
@ : -- calling or double colon followed by space for e.g 'n: ' called as 'type hint' or annotation
to Python that variable in the left called 'n' should be an int but unfortunately Python 
does not care about it.

@ this will be used by using Mypy to find error.
"""
