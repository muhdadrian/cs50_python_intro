def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()

#*args -- to allow the yell function to accept any number of arguments
#*args replaced with *words inside the yell function for specificity word instead of generic one.
#treat yell() just like print().