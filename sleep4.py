def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock



if __name__ == "__main__":
    main()

"""
@ This will never generate 1,000,000 sheep. Use 'yield' instead. 
@ yield - means return one value at a time (the for loop will keep on working)
"""