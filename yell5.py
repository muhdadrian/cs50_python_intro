def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()

"""
@ map(function, iterable, ...)

@ uppercased = map(str.upper, words) -- the return value of the map function that takes two arguments,
to map. The str class there is function called upper. 
"""